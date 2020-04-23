from .engineobj import SqEngineObject


class MlagObj(SqEngineObject):

    def summarize(self, **kwargs):
        """Summarize MLAG info"""

        self._summarize_on_add_field = [
            ('deviceCnt', 'hostname', 'nunique'),
            ('uniqueSystemIdCnt', 'systemId', 'nunique')
        ]

        self._summarize_on_add_with_query = [
            ('hostsWithfailedStateCnt', 'state != "active"', 'state'),
            ('hostsWithBackupInactiveCnt', 'state == "active"', 'backupActive')
        ]

        self._summarize_on_add_stat = [
            ('mlagNumDualPortsStat', 'state == "active"', 'mlagDualPortsCnt'),
            ('mlagNumSinglePortStat', 'state == "active"', 'mlagSinglePortsCnt'),
            ('mlagNumErrorPortStat', 'state == "active"', 'mlagErrorPortsCnt')
        ]

        return super().summarize(**kwargs)
