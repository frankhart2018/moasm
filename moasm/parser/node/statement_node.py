from abc import abstractmethod

from .node import Node


class StatementNode(Node):
    @abstractmethod
    def late_bind(self, bind_node: 'StatementNode') -> None:
        pass