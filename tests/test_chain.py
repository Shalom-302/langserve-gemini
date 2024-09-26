from langserve_launch_example import ask_question


def test_my_chain() -> None:
    """Edit this test to test your chain."""
    from langchain.llms.human import HumanInputLLM

    llm = HumanInputLLM(input_func=lambda *args, **kwargs: "foo")
    chain = ask_question(llm)
    chain.invoke({"text": "foo"})
