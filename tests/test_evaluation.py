"""Offline rubric/reference functions; no actual model or MCP invocation."""
import copy
import json
import unittest
from pathlib import Path


def usable(scope, m):
    if any(m.get(k) != scope[k] for k in ('tenant','slug','from','to')):
        return False
    if m.get('unit') != m.get('expected_unit'):
        return False
    points=m.get('points',[])
    dates=[d for d,v in points]
    return bool(points) and len(set(dates))==len(dates) and dates==sorted(dates) and all(
        scope['from']<=d<=scope['to'] and isinstance(v,(int,float)) and v>0 for d,v in points)


def chart(points, renderer):
    valid=[(d,v) for d,v in points if v is not None]
    if len(valid)<2: return {'status':'unavailable','points':[]}
    return {'status':'chart' if renderer else 'table','points':points}


def response_errors(r, evidence, mode='daily'):
    errors=[]
    if len(r['rendered'].split())>(350 if mode=='daily' else 700): errors.append('verbose')
    if len(r['verdict'].split())>30: errors.append('verdict')
    if len(r['experiments'])>3: errors.append('too_many_experiments')
    for c in r['claims']:
        e=evidence.get(c['source'])
        if not e or not e['usable'] or (c['date'],c['value']) not in e['points']: errors.append('unsupported_claim')
    if r.get('chart'):
        e=evidence.get(r['chart']['source'])
        if not e or not e['usable'] or r['chart']['points']!=e['points']: errors.append('invented_series')
    for a in r['experiments']:
        required=('source','problem','specific_change','effort','metric','baseline','review_window','stop')
        if any(a.get(k) in (None,'') for k in required): errors.append('incomplete_experiment')
        e=evidence.get(a.get('source'))
        if not e or not e['usable']: errors.append('unsupported_experiment')
        if a.get('metric') not in ('rank','review_events','downloads','resolved_share','manual_reproduction'): errors.append('unavailable_metric')
        if a.get('specific_change','').lower() in ('improve seo','engage users','optimize onboarding'): errors.append('generic_change')
    return errors


class Evaluation(unittest.TestCase):
    def setUp(self):
        self.e={'R1':{'usable':True,'points':[('2026-10-09',18),('2026-10-15',24)]}}
        self.r={'rendered':'Rank worsened six positions. Draft a clearer listing benefit after inspecting current copy.',
                'verdict':'Acorn lost visibility; validate listing intent before editing.',
                'claims':[{'source':'R1','date':'2026-10-15','value':24}],
                'chart':{'source':'R1','points':self.e['R1']['points']},
                'experiments':[{'source':'R1','problem':'Acorn lost six rank positions','specific_change':'Inspect simple forms intent and draft one truthful listing opening sentence','effort':'S estimate','metric':'rank','baseline':24,'review_window':'2026-10-22 UTC','stop':'Pause on missing coverage'}]}

    def test_mismatched_and_missing_data_fixtures(self):
        f=json.loads((Path(__file__).parent/'fixtures/evidence-cases.json').read_text())
        for c in f['cases']:
            with self.subTest(c['name']): self.assertEqual(usable(f['scope'],c['metric']),c['usable'])

    def test_concise_supported_action_passes(self):
        self.assertEqual(response_errors(self.r,self.e),[])

    def test_verbose_daily_is_rejected_but_deep_can_fit(self):
        self.r['rendered']='word '*351
        self.assertIn('verbose',response_errors(self.r,self.e))
        self.assertNotIn('verbose',response_errors(self.r,self.e,'deep'))
        self.r['rendered']='word '*701
        self.assertIn('verbose',response_errors(self.r,self.e,'deep'))

    def test_invalid_evidence_blocks_claim_and_experiment(self):
        self.e['R1']['usable']=False
        self.assertIn('unsupported_claim',response_errors(self.r,self.e))
        self.assertIn('unsupported_experiment',response_errors(self.r,self.e))

    def test_invented_chart_point_fails(self):
        self.r['chart']['points']=self.e['R1']['points']+[('2026-10-10',20)]
        self.assertIn('invented_series',response_errors(self.r,self.e))

    def test_missing_day_not_interpolated_and_host_fallback(self):
        p=[('2026-10-09',18),('2026-10-10',None),('2026-10-11',24)]
        self.assertEqual(chart(p,True)['points'],p)
        self.assertEqual(chart(p,False),{'status':'table','points':p})
        self.assertEqual(chart(p[:2],True)['status'],'unavailable')

    def test_generic_or_unmeasurable_action_fails(self):
        a=self.r['experiments'][0];a['specific_change']='improve SEO';a['metric']='conversion';a['review_window']=''
        self.assertTrue({'generic_change','unavailable_metric','incomplete_experiment'}<=set(response_errors(self.r,self.e)))

    def test_more_than_three_actions_fails(self):
        self.r['experiments']*=4
        self.assertIn('too_many_experiments',response_errors(self.r,self.e))

    def test_milestone_inconsistent_bucket_rejected(self):
        # No exact distance may be computed from a public band.
        def distance(current,next_value,unit):
            return next_value-current if unit=='exact_count' and next_value>current else None
        self.assertIsNone(distance(10000,5000,'exact_count'))
        self.assertIsNone(distance(10000,20000,'coarse_band'))

    def test_stale_competitor_not_comparable(self):
        def comparable(a,b):
            return all(a[k]==b[k] for k in ('from','to','unit')) and a['age']<=36 and b['age']<=36
        a={'from':'2026-10-09','to':'2026-10-15','unit':'rank','age':2}
        b=copy.deepcopy(a);b['age']=48
        self.assertFalse(comparable(a,b));b['age']=2;b['unit']='stars';self.assertFalse(comparable(a,b))
