from multiprocessing.queues import Queue
import multiprocessing


class UdderQueue(Queue):
    def __init__(self,
                 num_feeders: int = 1,
                 name: str = "UdderQueue",
                 context: str = "spawn",):
        self.parse_arguments(num_feeders, name, context)
        super().__init__(maxsize=0, ctx=multiprocessing.get_context(context))
        self.num_feeders = num_feeders

    def __str__(self):
        return self.name

    def parse_arguments(self,
                        num_feeders: int,
                        name: str,
                        context: str,):
        context_options = ['spawn', 'fork', 'forkserver']
        if context not in context_options:
            raise ValueError(
                    f":param 'context' must be one of {context_options}")
        if num_feeders <= 0:
            raise ValueError(f":param 'num_feeders' must be >0")

    def put(self, contents=None, block=True, timeout=None):
        raise NotImplementedError("Implement")

    def put_nowait(self, contents=None):
        raise NotImplementedError("Implement")

    def get(self, block=True, timeout=None):
        raise NotImplementedError("Implement")

    def get_nowait(self):
        raise NotImplementedError("Implement")
