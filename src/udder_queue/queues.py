from multiprocessing.queues import Queue
from multiprocessing import Lock
import multiprocessing


class UdderQueue(Queue):
    def __init__(self,
                 name: str = "UdderQueue",
                 num_feeders: int = 1,
                 context: str = "spawn",):
        self.name = name
        self.parse_arguments(num_feeders, name, context)
        Queue.__init__(maxsize=0, ctx=multiprocessing.get_context(context))
        self.num_feeders = num_feeders
        self.lock = Lock

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
            raise ValueError(f":param 'num_feeders' must be > 0")

    def put(self, contents=None, block=True, timeout=None):
        raise NotImplementedError("Implement")

    def put_nowait(self, contents=None):
        raise NotImplementedError("Implement")

    def get(self, block=True, timeout=None):
        raise NotImplementedError("Implement")

    def get_nowait(self):
        raise NotImplementedError("Implement")


# class MonoQueue(Queue):
#     '''
#     Queue based on multiprocessing.queues.Queue with constrained size of 1
#     '''
#     def __init__(self):
#         Queue.__init__(self,
#                        maxsize=1,
#                        ctx=multiprocessing.get_context("spawn"))
#         self.lock = Lock()
#
#     def put(self, contents: QT, block=True, timeout=None):
#         '''
#         put in queue, replacing current contents if there is something to
#         replace.
#
#         blocking
#         '''
#         self.lock.acquire()
#         while not self.empty():
#             Queue.get(self, block=False)
#         # NOTE/TODO: this, because multiprocessing Queues are stupid, is
#         # necessary. Explained in short, if you try to q.put_nowait() too
#         # quickly, it breaks. For example, say you were in ipython,
#         # and you typed to following
#         # - q = MonoQueue()
#         # - q.put_nowait(2)
#         # - q.put_nowait(3)
#         # - q.put_nowait(4)
#         # - q.put_nowait(5)
#         # EVEN THOUGH there is a Lock() to atomize the access to the Queue,
#         # one of the non-first 'put_nowait()' calls will acquire the lock,
#         # the 'self.empty()' call is apparently True, even though something
#         # is actually in the queue, and then it will not '.get()' it and try
#         # to put something in the queue, raise a 'Full' exception.
#         # So basically, apparently if something tries to put in the queue too
#         # quickly, everything breaks. And yes, I made a pytest to test this,
#         # guess what, if you try to run a trace (debugger), aka you jus step
#         # through, it works fine, but as soon as you just run it, it breaks.
#         # UGH, maybe I'm dumb and am doing something wrong
#         with suppress(Full):
#             Queue.put(self, contents, block=block, timeout=timeout)
#         self.lock.release()
#
#     def put_nowait(self, contents: QT):
#         '''
#         put in queue, replacing current contents if there is something to
#         replace.
#
#         non-blocking
#         '''
#         self.put(contents, block=False)
#
#     def get_nowait(self) -> QT:
#         '''
#         get from queue
#
#         non-blocking
#         '''
#         self.lock.acquire()
#         contents = None
#         with suppress(Empty):
#             contents = Queue.get(self, block=False)
#         self.lock.release()
#         return contents
#
#     def get(self, block=True, timeout=None) -> QT:
#         '''
#         get from queue
#
#         blocking
#         '''
#         return Queue.get(self, block=True, timeout=timeout)
#
#
# class UnlimitedQueue(Queue):
#     '''
#     Queue based on multiprocessing.queues.Queue with unconstrained size
#     '''
#     def __init__(self):
#         Queue.__init__(self, ctx=multiprocessing.get_context('spawn'))
#
#     def put(self, contents: QT, block=True, timeout=None):
#         '''
#         blocking
#         '''
#         Queue.put(self, contents, block=block, timeout=timeout)
#
#     def put_nowait(self, contents: QT):
#         '''
#         non-blocking
#         '''
#         self.put(contents, block=False)
#
#     def get_nowait(self) -> QT:
#         '''
#         non-blocking
#         '''
#         contents = None
#         with suppress(Empty):
#             contents = Queue.get(self, block=False)
#         return contents
#
#     def get(self, timeout=None) -> QT:
#         '''
#         blocking
#         '''
#         return Queue.get(self, block=True, timeout=timeout)
