class Greeting:
    def main(self) -> str:
        return "Hello Sajeel, who are you?"
    

class Identity:
    def main(self) -> str:
        return "My name is Sajeel"
    

def call_class(obj):
    print(obj.main())


greeting_instance: Greeting = Greeting()
identity_instance: Identity = Identity()

call_class(greeting_instance)
call_class(identity_instance)


