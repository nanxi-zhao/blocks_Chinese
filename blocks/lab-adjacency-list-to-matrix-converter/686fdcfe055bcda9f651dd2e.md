---
id: 686fdcfe055bcda9f651dd2e
title: 构建邻接表到矩阵转换器
challengeType: 27
dashedName: build-an-adjacency-list-to-matrix-converter
---

# --description--

在这个实验中，你将构建一个函数，将图的邻接表表示转换为邻接矩阵。邻接表是一个字典，其中每个键代表一个节点，对应的值是该键节点连接到的节点列表。邻接矩阵是一个二维数组，如果从节点`i`到节点`j`有一条边，则位置`[i][j]`处的条目为`1`，否则为`0`。

例如，给定邻接表：

```py
{
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}
```

对应的邻接矩阵将是：

```py
[
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 0, 1, 0]
]
```

**目标：** 实现以下用户需求并通过所有测试以完成实验。

**用户需求：**

1. 你应该定义一个名为`adjacency_list_to_matrix`的函数来将邻接表转换为邻接矩阵。
2. 该函数应该接受一个表示无权图（有向或无向）邻接表的字典作为其参数。
3. 该函数应该：
   - 将邻接表转换为邻接矩阵。
   - 打印邻接矩阵中的每一行。
   - 返回邻接矩阵。

例如，`adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})`应该打印：

```md
[0, 0, 1, 0]
[0, 0, 1, 1]
[1, 1, 0, 1]
[0, 1, 1, 0]
```

并返回`[[0, 0, 1, 0], [0, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]`。


# --hints--

你应该定义一个名为`adjacency_list_to_matrix`的函数。

```js
({ 
    test: () => assert(runPython(`
    _Node(_code).has_function("adjacency_list_to_matrix")
    `)) 
})
```

`adjacency_list_to_matrix`函数应该有一个参数。

```js
({ test: () => assert(runPython(`
    import inspect 
    sig = inspect.signature(adjacency_list_to_matrix)
    len(sig.parameters) == 1
  `))
})
```

该函数应该能够从邻接表中正确确定节点数量。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [1], 1: [0], 2: []}
        result = adjacency_list_to_matrix(adj_list)
        assert len(result) == 3
        assert len(result[0]) == 3
    `) 
})
```

该函数应该正确地将矩阵值设置为`1`表示存在的边。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [1], 1: [0]}
        result = adjacency_list_to_matrix(adj_list)
        assert result[0][1] == 1
        assert result[1][0] == 1
        assert result[0][0] == 0
        assert result[1][1] == 0
    `) 
})
```

该函数应该打印矩阵的每一行。

```js
({ 
    test: () => runPython(`
        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        adj_list = {0: [1], 1: []}
        adjacency_list_to_matrix(adj_list)

        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()

        assert "[0, 1]" in output
        assert "[0, 0]" in output
    `) 
})
```

该函数应该返回邻接矩阵。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [1], 1: []}
        result = adjacency_list_to_matrix(adj_list)
        assert result == [[0, 1], [0, 0]]
    `) 
})
```

当给定邻接表`{0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}`时，该函数应该返回`[[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]`。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}
        result = adjacency_list_to_matrix(adj_list)
        expected = [[0, 1, 1, 0], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 1, 0]]
        assert result == expected
    `) 
})
```

当给定邻接表`{0: [1], 1: [0]}`时，该函数应该返回`[[0, 1], [1, 0]]`。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [1], 1: [0]}
        result = adjacency_list_to_matrix(adj_list)
        expected = [[0, 1], [1, 0]]
        assert result == expected
    `) 
})
```

当给定邻接表`{0: [], 1: [], 2: []}`时，该函数应该返回`[[0, 0, 0], [0, 0, 0], [0, 0, 0]]`。

```js
({ 
    test: () => runPython(`
        adj_list = {0: [], 1: [], 2: []}
        result = adjacency_list_to_matrix(adj_list)
        expected = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        assert result == expected
    `) 
})
```

# --seed--

## --seed-contents--

```py

```

# --solutions--

```py
def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)

    adj_matrix = [[0] * n for _ in range(n)]

    for src_node, neighbors in adj_list.items(): 
        for dest_node in neighbors:
            adj_matrix[src_node][dest_node] = 1

    for row in adj_matrix:
        print(row)

    return adj_matrix

adj_list = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [2]
}

matrix = adjacency_list_to_matrix(adj_list)
```