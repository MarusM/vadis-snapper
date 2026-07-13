# ============================================================
# V.A.D.I.S. Snapper
#
# Module:
# session.py
#
# Responsibility:
# Provides a unique session identifier for the
# current application run.
#
# ============================================================

from datetime import datetime


SESSION_ID = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")