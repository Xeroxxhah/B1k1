import math
from threading import Thread


class ThreadManager:

    def __init__(self):
        self.files_per_thread = 5
        self.calculated_threads = None
    
    def CalculateThreads(self, no_of_paths, files_in_thread=5):
        partially_calculated_threads = no_of_paths / files_in_thread
        if partially_calculated_threads <= 5:
            if isinstance(partially_calculated_threads, float):
                partially_calculated_threads = math.ceil(partially_calculated_threads)
            self.calculated_threads = partially_calculated_threads
        else:
            self.files_per_thread *= 2
            CalculateThreads(no_of_paths, files_in_thread=self.files_per_thread)
    
    def Slice(self,list_of_paths,no_of_threads):
        for x in range(0, len(list_of_paths), no_of_threads):
            yield list_of_paths[x:x + no_of_threads]


    def ThreadFactory(self,path_iter,backup_path,func):
        thread_list = []
        path_list = list(path_iter)
        for x in range(0,self.calculated_threads):
            thread_list.append(Thread(target=func, args=(path_list,backup_path,)))
        return thread_list

    

    


