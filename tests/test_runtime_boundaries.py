"""Fictional reference decisions, not a model or native-chart runtime test."""
import unittest
from datetime import date


def period_label(observed, start, end, as_of):
    if observed is None: return 'undated total'
    value=date.fromisoformat(observed)
    if value>date.fromisoformat(as_of): return 'quarantined future'
    if value<date.fromisoformat(start): return 'historical'
    if value>date.fromisoformat(end): return 'excluded post-window'
    return 'current period'


def source_timezone(date_only, documented_timezone=None):
    return documented_timezone if documented_timezone else 'unknown'


def comparable_estimates(a,b):
    return not a['cached'] and not b['cached'] and a['window']==b['window'] and a['unit']==b['unit']


def render_decision(valid_points, attempt):
    if valid_points<2: return 'trend unavailable; renderer unassessed'
    if attempt is None: return 'test supported native renderer'
    return 'chart' if attempt=='success' else 'dated table; renderer limitation disclosed'


class RuntimeBoundaries(unittest.TestCase):
    def test_old_reviews_are_historical(self):
        self.assertEqual(period_label('2026-09-01','2026-10-09','2026-10-15','2026-10-16'),'historical')
        self.assertEqual(period_label('2026-10-15','2026-10-09','2026-10-15','2026-10-16'),'current period')

    def test_undated_total_is_not_current_period(self):
        self.assertEqual(period_label(None,'2026-10-09','2026-10-15','2026-10-16'),'undated total')

    def test_date_only_does_not_imply_utc(self):
        self.assertEqual(source_timezone('2026-10-15'),'unknown')
        self.assertEqual(source_timezone('2026-10-15','UTC'),'UTC')

    def test_cached_estimates_not_same_window_evidence(self):
        a={'cached':True,'window':'2026-10-09/2026-10-15','unit':'approx_installs'}
        b=dict(a,cached=False)
        self.assertFalse(comparable_estimates(a,b))

    def test_renderer_requires_actual_attempt_and_valid_data(self):
        self.assertEqual(render_decision(0,None),'trend unavailable; renderer unassessed')
        self.assertEqual(render_decision(2,None),'test supported native renderer')
        self.assertEqual(render_decision(2,'success'),'chart')
        self.assertEqual(render_decision(2,'unsupported'),'dated table; renderer limitation disclosed')

    def test_named_color_legend_matches_series(self):
        def legend_ok(series,legend):
            return set(series)==set(legend) and all(legend[n]['label']==n and legend[n]['color'] for n in series)
        series={'Acorn':[("2026-10-15",11)],'Cedar':[("2026-10-15",14)]}
        good={'Acorn':{'label':'Acorn','color':'blue'},'Cedar':{'label':'Cedar','color':'orange'}}
        self.assertTrue(legend_ok(series,good))
        good['Acorn']['label']='first line';self.assertFalse(legend_ok(series,good))

    def test_observational_timing_does_not_establish_or_exclude_cause(self):
        def causal_label(evidence):
            return 'candidate explanation identified' if evidence=='observational timing' else 'insufficient causal evidence'
        result=causal_label('observational timing')
        self.assertEqual(result,'candidate explanation identified')
        self.assertNotIn(result,('cause found','cause ruled out'))


    def test_post_window_and_future_are_not_historical(self):
        self.assertEqual(period_label('2026-10-16','2026-10-09','2026-10-15','2026-10-16'),'excluded post-window')
        self.assertEqual(period_label('2026-10-17','2026-10-09','2026-10-15','2026-10-16'),'quarantined future')
