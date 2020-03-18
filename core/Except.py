def syntax_error(*args, agent):
    try:
        if hasattr(agent, "lexer"):
            raise SyntaxError(
                f"님 코드 개이상하네요;\n"
                f"File '{agent.program_object.name}', line {agent.line + 1}\n"
                f"  =>{agent.lexer.lines[agent.line]}\n"
                "\n우리집 고양이가 해도 님보단 잘하겠네요.\n"
                "아 그런데 뭐가 문제인지는 모르겠어요 !"
            )

    except Exception as err:
        print(*args)
        exit(err)
