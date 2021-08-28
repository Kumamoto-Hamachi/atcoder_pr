# Atcoder研究ノート ~緑への道~
*参考文献
[レッドコーダーが教える、競プロ・AtCoder上達のガイドライン【中級編：目指せ水色コーダー！】](https://qiita.com/e869120/items/eb50fdaece12be418faa)

# 1. 全探索:TODO
## 1.1 全列挙
- 参考文献
[たのしい探索アルゴリズムの世界【前編：全探索、bit全探索から半分全列挙まで】 の 2 章](https://qiita.com/e869120/items/25cb52ba47be0fd418d6#2-%E3%81%99%E3%81%B9%E3%81%A6%E3%81%AE%E5%9F%BA%E6%9C%AC%E5%85%A8%E6%8E%A2%E7%B4%A2)
全探索は「全てのあり得る通り数を探索する」ということ.
全探索で最も重要なことは、「通り数をしっかり見積もること」です.
[実例]
abc106_b
abc136_b
abc68_b
abc133_b
三井住友銀行プログラミングコンテスト2019_b
M-SOLUTIONSプロコンオープン2020_b(別解あり)
abc105_b
abc157_c

- 全探索の工夫パターン3個
(1)既に分かっているものは解かない
例えば,「一部探索しただけで他が一意に定まる」性質を用いて全探索を節約する.
abc95_c
abc112_c
(2)探索の通り数を絞り込む
abc57_c
square869120Contest_#6_b.py
(3)別の視点から全探索する
三井住友信託銀行プログラミングコンテスト2019_c-100 to 105 #TODO 動的計画法でも
abc89_c


## 1.2 bit全探索
[p進法展開](http://shochandas.xsrv.jp/p-exp/p-exp.htm)
2進数変換するアルゴリズム.py
[ビット演算](https://note.nkmk.me/python-bit-operation/)
論理積(AND): &
論理和(OR): |
排他的論理和(XOR): ^
ビット反転(NOT): ~
ビットシフト: <<, >>
[実例]
abc128_c
abc147_c #TODO 深さ優先探索と二重配列を使った別解 あと書きかけ
abc167_c
square869120Contest#4_b #TODO シンプルに解けない(別日に解くこと)
## 1.3 順列全探索
itertools.permutations
[実例]
abc145_c
abc150_c # コーナーケース(同じ,端等の変わったケースをちゃんと考えよう)
abc54_c # TODO もう一回書いて
## 1.4 再帰関数を用いた全探索(深さ優先探索)
*参考文献
[再帰関数を学ぶと、どんな世界が広がるか](https://qiita.com/drken/items/23a4f604fa3f505dd5ad)
[動的計画法超入門！ Educational DP Contest の A ～ E 問題の解説と類題集](https://qiita.com/drken/items/dc53c683d6de8aeacf5a) # TODO

```
戻り値の型 func(引数) {
  if (ベースケース) {
    return ベースケースに対する値;
  }

  func(次の引数); // 再帰呼び出しします。その前後でも色々やります。
  return (答え);
}
```
複数再帰呼び出しを行うと,計算量が爆発する.
メモ化
[実例]
sum_fibo_recursion.py
再帰出ないと厳しい問題もある.
例えば,(1)部分和問題(2)数独ソルバー(3)グラフ上の探索
[実例]
