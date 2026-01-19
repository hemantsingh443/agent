from llm import call_llm
from schema import Reflection
from log import log

REFLECT_PROMPT = """
You are a critic.

Evaluate whether the result correctly solves the original goal.

Respond ONLY in valid JSON:
{
  "is_correct": true | false,
  "reason": "..."
}
"""

def reflect(goal: str, result: str) -> Reflection: 
    log("REFLECTION INPUT", f"Goal: {goal}\nResult: {result}")
    messages = [
        {"role": "system", "content": REFLECT_PROMPT},
        {"role": "user", "content": f"Goal: {goal}\nResult: {result}"},
    ]
    raw = call_llm(messages)

    log("RAW REFLECTION OUTPUT", raw)

    reflection = Reflection.model_validate_json(raw)

    log(
        "REFLECTION RESULT",
        f"Correct: {reflection.is_correct}\nReason: {reflection.reason}"
    )

    return reflection
