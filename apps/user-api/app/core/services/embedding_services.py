# from typing import Any, Dict, List

# from langchain.schema import Document
# from langchain.vectorstores import Qdrant
# from qdrant_client import QdrantClient

# from services.langchain_services import embeddings


# class QdrantService:

#     def __init__(
#         self,
#         db_path: str,
#         collection_name: str,
#     ):
#         self.db_path = db_path
#         self.collection_name = collection_name

#     def save_documents(self, documents: List[Document]) -> None:
#         chunk_size = 10
#         for i in range(0, len(documents), chunk_size):
#             chunk_documents = documents[i : i + chunk_size]  # noqa: E203
#             Qdrant.from_documents(
#                 chunk_documents,
#                 embeddings,
#                 path=self.db_path,
#                 collection_name=self.collection_name,
#             )

#     def get_documents(
#         self,
#         user_input: str,
#         metadata_filter: Dict[str, Any],
#         k=30,
#     ):
#         index_client = QdrantClient(path=self.db_path)
#         vector = Qdrant(index_client, self.collection_name, embeddings)
#         return vector.similarity_search(user_input, k=k, filter=metadata_filter)

#     def get_documents_with_score(
#         self,
#         user_input: str,
#         metadata_filter: Dict[str, Any],
#         k=30,
#     ):
#         index_client = QdrantClient(path=self.db_path)
#         vector = Qdrant(index_client, self.collection_name, embeddings)
#         return vector.similarity_search_with_score(
#             user_input, k=k, filter=metadata_filter
#         )
