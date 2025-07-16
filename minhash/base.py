import hashlib
import random
import numpy as np
from typing import List, Set, Union

class MinHash:
    def __init__(self, num_perm: int = 128, seed: int = 1):
        """
        MinHash 객체를 초기화합니다.
        
        Args:
            num_perm: 해시 함수의 개수 (순열의 개수)
            seed: 난수 생성을 위한 시드값
        """
        self.num_perm = num_perm
        self.seed = seed
        self.hash_values = None
        
        # 해시 함수를 위한 랜덤 계수들 생성
        random.seed(seed)
        np.random.seed(seed)
        
        # ax + b (mod p) 형태의 해시 함수를 위한 계수들
        self.a = np.random.randint(1, 2**31 - 1, size=num_perm, dtype=np.int64)
        self.b = np.random.randint(0, 2**31 - 1, size=num_perm, dtype=np.int64)
        
        # 큰 소수 (해시 함수의 모듈로 연산용)
        self.prime = 2**31 - 1
        
        # MinHash 값들을 저장할 배열
        self.hash_values = np.full(num_perm, np.inf, dtype=np.float64)
    
    def _hash(self, item: Union[str, bytes]) -> int:
        """
        문자열이나 바이트를 정수로 해시합니다.
        """
        if isinstance(item, str):
            item = item.encode('utf-8')
        return int(hashlib.md5(item).hexdigest(), 16)
    
    def update(self, item: Union[str, bytes]):
        """
        새로운 아이템으로 MinHash를 업데이트합니다.
        """
        hash_val = self._hash(item)
        
        # 각 해시 함수에 대해 최소값 업데이트
        for i in range(self.num_perm):
            perm_hash = (self.a[i] * hash_val + self.b[i]) % self.prime
            self.hash_values[i] = min(self.hash_values[i], perm_hash)
    
    def update_batch(self, items: List[Union[str, bytes]]):
        """
        여러 아이템들로 MinHash를 한 번에 업데이트합니다.
        """
        for item in items:
            self.update(item)
    
    def jaccard_similarity(self, other: 'MinHash') -> float:
        """
        다른 MinHash와 Jaccard 유사도를 계산합니다.
        """
        if self.num_perm != other.num_perm:
            raise ValueError("두 MinHash의 순열 수가 다릅니다.")
        
        # 같은 해시값을 가진 순열의 개수 계산
        matches = np.sum(self.hash_values == other.hash_values)
        return matches / self.num_perm
    
    def merge(self, other: 'MinHash') -> 'MinHash':
        """
        두 MinHash를 병합합니다.
        """
        if self.num_perm != other.num_perm:
            raise ValueError("두 MinHash의 순열 수가 다릅니다.")
        
        merged = MinHash(self.num_perm, self.seed)
        merged.a = self.a.copy()
        merged.b = self.b.copy()
        merged.hash_values = np.minimum(self.hash_values, other.hash_values)
        return merged
    
    def reset(self):
        """
        MinHash를 초기 상태로 리셋합니다.
        """
        self.hash_values = np.full(self.num_perm, np.inf, dtype=np.float64)
    
    def __eq__(self, other: 'MinHash') -> bool:
        """
        두 MinHash가 같은지 확인합니다.
        """
        return np.array_equal(self.hash_values, other.hash_values)
    
    def __len__(self) -> int:
        """
        순열의 개수를 반환합니다.
        """
        return self.num_perm


def create_minhash_from_set(items: Set[Union[str, bytes]], num_perm: int = 128) -> MinHash:
    """
    집합으로부터 MinHash 객체를 생성합니다.
    """
    minhash = MinHash(num_perm)
    minhash.update_batch(list(items))
    return minhash


def jaccard_similarity_exact(set1: Set, set2: Set) -> float:
    """
    두 집합의 정확한 Jaccard 유사도를 계산합니다. (비교용)
    """
    intersection = len(set1 & set2)
    union = len(set1 | set2)
    return intersection / union if union > 0 else 0.0

if __name__ == "__main__":
    # 집합 생성
    set1 = {"apple", "banana", "cherry", "date"}
    set2 = {"apple", "banana", "elderberry", "fig"}

    # MinHash 생성
    mh1 = create_minhash_from_set(set1)
    mh2 = create_minhash_from_set(set2)

    # 유사도 계산
    similarity = mh1.jaccard_similarity(mh2)
    print(f"MinHash 유사도: {similarity:.4f}")

    # 정확한 유사도와 비교
    exact_similarity = jaccard_similarity_exact(set1, set2)
    print(f"정확한 유사도: {exact_similarity:.4f}")