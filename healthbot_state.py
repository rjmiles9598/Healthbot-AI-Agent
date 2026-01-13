
# This is a file containing the healthbot application state schema

from langgraph.graph import MessagesState
from typing import List, Optional, Dict, Any, Literal

class State(MessagesState):
    topic: Optional[str]
    summary: Optional[str]
    quiz_question: Optional[str]
    quiz_correct_option: Optional[str]
    patient_answer: Optional[str]
    evaluation: Optional[Dict[str, Any]]
    phase: Optional[
        Literal[
            "ask_topic",
            "searching",
            "show_summary",
            "waiting_ready",
            "quiz_generated",
            "waiting_answer",
            "evaluated",
            "waiting_restart"
        ]
    ]
    repeat_mode: bool
