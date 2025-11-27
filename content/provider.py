
from typing import Dict, Tuple
from abc import ABC, abstractmethod


class ContentProvider(ABC):
    """
    Abstract Base Class defining the interface for a content retrieval system.
    
    This interface mandates a contract for fetching content and its associated 
    metadata from an external source or cache using a unique identifier.
    """

    @abstractmethod
    def retrieve(self, identifier: str) -> Tuple[Dict[str, any], str]:
        """
        Obtains the content and associated properties for the provided identifier.

        Args:
            identifier (str): The location identifier for the resource.

        Returns:
            Tuple[Dict[str, any], str]: A tuple containing the document metadata and document content.

        Raises:
            Exception: If the content cannot be obtained from the source.
        """
        raise NotImplementedError

    @staticmethod
    def get_implementation() -> 'ContentProvider':
        """
        Factory method to obtain the active content provider instance.

        Returns:
            ContentProvider: An instance of the concrete content provider implementation.
        """
        
        import content.web_content_provider
        return content.web_content_provider.WebContentProvider()

