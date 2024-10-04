from abc import ABC, abstractmethod

class train_interface(ABC):
    __train_id = -1
    __train_name = ""
    __start = ""
    __destination = ""
    __route = []
    
    @abstractmethod
    def 