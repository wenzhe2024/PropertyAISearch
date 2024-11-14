from tools.memory_manager import MemoryManager
from models.role_play import RolePlay

class DialogueManager:
    def __init__(self):
        self.memory = MemoryManager()
        self.role_play = RolePlay()
        self.current_stage = "greeting"  # 初始阶段为问候阶段

    def handle_user_input(self, user_input):
        # 根据当前对话阶段选择不同的对话策略
        if self.current_stage == "greeting":
            response = self.role_play.greeting_stage(user_input)
            self.current_stage = "collect_requirements"
        
        elif self.current_stage == "collect_requirements":
            response = self.role_play.collect_requirements_stage(user_input)
            self.memory.update_context("user_requirements", response)
            self.current_stage = "recommendation"
        
        elif self.current_stage == "recommendation":
            requirements = self.memory.get_context("user_requirements")
            response = self.role_play.recommendation_stage(user_input, requirements)
            self.current_stage = "follow_up"
        
        elif self.current_stage == "follow_up":
            response = self.role_play.follow_up_stage(user_input)
            # 可以根据用户反馈重新进入推荐阶段或结束对话
            self.current_stage = "end" if self.role_play.should_end_dialogue(user_input) else "recommendation"
        
        else:
            response = "感谢您的咨询！欢迎随时联系我。"
        
        return response
