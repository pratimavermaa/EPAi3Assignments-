
from functools import lru_cache
from session10 import Polygon as pgn

class Polygon_Sequence:

    def __init__(self,no_edges,circumradius):
        self.no_edges = no_edges
        self.circumradius = circumradius
        self.ratios = dict()

    def __len__(self):
        return self.no_edges
    
    def __repr__(self)->str:
        if bool(self.ratios):
            data = [f"{key}:{value}\n" for key,value in self.ratios.items()]
            dict_info =''.join(data)
        else:
            dict_info = "Empty Dictionary"
        stat = f"Total {self.no_edges} Polygons with circumradius as {self.circumradius}"
        return f"{stat}\n {dict_info}"

    def __getitem__(self,vertex:int)->float:
        if isinstance(vertex, int):
            if vertex < 0:
                vertex = self.no_edges + vertex
            if vertex < 0 or vertex >= self.no_edges:
                raise IndexError
            else:
                if vertex>1:
                    return Polygon_Sequence._ratio(vertex,self.circumradius)
                else:
                    return 'it is not a polygon'
        else:
            raise IndexError
            
    @staticmethod
    @lru_cache(2 ** 10)
    def _ratio(no_edges:int,circumradius:int)->float:
        if no_edges < 2:
            return 1
        else:
            p1 = pgn(no_edges,circumradius)
            return p1.area/p1.perimeter
    
    @property
    def max_efficieny(self)->str:
        for i in range(self.no_edges):
            if i> 1:
                self.ratios[i+1] = self.__getitem__(i)
        key = max(self.ratios,key = self.ratios.get)
        return f"Max Ratio is {self.ratios[key]} at vertex {key}"
