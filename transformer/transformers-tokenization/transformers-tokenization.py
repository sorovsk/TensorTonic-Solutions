import numpy as np
from typing import List, Dict

class SimpleTokenizer:
    def __init__(self):
        self.word_to_id: Dict[str, int] = {}
        self.id_to_word: Dict[int, str] = {}
        self.vocab_size = 0

        self.pad_token = "<PAD>"
        self.unk_token = "<UNK>"
        self.bos_token = "<BOS>"
        self.eos_token = "<EOS>"

    def build_vocab(self, texts: List[str]) -> None:
        # 清空现有词汇表
        self.word_to_id.clear()
        self.id_to_word.clear()
        self.vocab_size = 0

        # 添加特殊标记，固定 ID 0-3
        special_tokens = [self.pad_token, self.unk_token, self.bos_token, self.eos_token]
        for idx, token in enumerate(special_tokens):
            self.word_to_id[token] = idx
            self.id_to_word[idx] = token
            self.vocab_size += 1

        # 收集所有单词（小写）
        word_set = set()
        for text in texts:
            for word in text.lower().split():   # 转为小写再分割
                word_set.add(word)

        # 排序后添加
        for word in sorted(word_set):
            if word not in self.word_to_id:
                self.word_to_id[word] = self.vocab_size
                self.id_to_word[self.vocab_size] = word
                self.vocab_size += 1

    def encode(self, text: str) -> List[int]:
        # 转为小写，按空白分割
        unk_id = self.word_to_id.get(self.unk_token, 1)  # 默认1
        ids = []
        for word in text.lower().split():
            ids.append(self.word_to_id.get(word, unk_id))
        return ids

    def decode(self, ids: List[int]) -> str:
        words = []
        for i in ids:
            words.append(self.id_to_word.get(i, self.unk_token))
        return " ".join(words)