"""Fictional reference decisions, not a model or native-chart runtime test."""
import unittest
from datetime import date


def period_label(observed, start, end):
    if observed is None: return 'undated total'
    return 'current period' if date.fromisoformat(start)<=date.fromisoformat(observed)<=date.fromisoformat(end) else 'historical'


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
        self.assertEqual(period_label('2026-09-01','2026-10-09','2026-10-15'),'historical')
        self.assertEqual(period_label('2026-10-15','2026-10-09','2026-10-15'),'current period')

    def test_undated_total_is_not_current_period(self):
        self.assertEqual(period_label(None,'2026-10-09','2026-10-15'),'undated total')

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
