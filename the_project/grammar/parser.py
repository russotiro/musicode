import lark

grammar_file = open("grammar.lark", "r")
parser = lark.Lark(grammar_file.read())

musicode_file = open("../simple_example.mc", "r")
tree = parser.parse(musicode_file.read())


print(tree.pretty())