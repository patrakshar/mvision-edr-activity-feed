"""
ESM11 subscription to Threat and Case entities:
Please notice that SysLogHandler is set locally and then its recommended to:
1.Point rsyslog.conf to REMOTE ESM
2.Enable TLS for secured communication instead of UDP
(ASP Passive DS must be enabled for TLS too so Threat evidence packets can't
be expossed to Man In de Middle attacks)
"""
import logging
from mvision_edr_activity_feed import subscribe


@subscribe(entity='case')
def any_case_event(event):
    logging.info("ESM CASE EVENT: %s", event)

@subscribe(entity='threat')
def any_case_event(event):
    logging.info("ESM THREAT EVENT: %s", event)
