#入力 a b c d e
a, b, c, d, e = map(int, input().split())
#個数わからないなら
a = list(map(int, input().split()))


#入力 a 
#   　b
#   　c
#   　d

a, b, c, d  = [int(input()) for _ in range(4)]

#こっちにすればlistで入る
a = [int(input()) for _ in range(4)]

#入力
# a1, b1, c1
# a2, b2, c2
# *
# *
# a3, b3, c3

# 各英語についてlistにする場合
abc = [map(int, input().split()) for _ in range(N)]
a, b, c = [list(i) for i in zip(*abc)]

#あるリストbに基づいてaをソートしたい場合
a = [i for _, i in sorted(zip(b, a))]

#行列で入れる場合
a = [list(map(int, input().split())) for l in range()]
