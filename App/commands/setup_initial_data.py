from django.core.management.base import BaseCommand
from App.models import Status, User, Task

class Command(BaseCommand):
    help = 'Configura dados iniciais do sistema (Status, usuários e tarefas de exemplo)'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('🚀 Configurando dados iniciais...'))
        
        # Criar status se não existirem
        status_names = ["Pendente", "Em Andamento", "Concluída"]
        created_status = []
        
        for name in status_names:
            status, created = Status.objects.get_or_create(name=name)
            if created:
                created_status.append(name)
                self.stdout.write(f"✅ Status '{name}' criado")
            else:
                self.stdout.write(f"ℹ️  Status '{name}' já existe")
        
        # Criar usuários de exemplo se não existirem
        users_data = [
            {"username": "joao", "password": "123456"},
            {"username": "maria", "password": "123456"},
            {"username": "admin", "password": "admin123"}
        ]
        
        created_users = []
        for user_data in users_data:
            user, created = User.objects.get_or_create(
                username=user_data["username"],
                defaults={'password': user_data["password"]}
            )
            if created:
                created_users.append(user_data["username"])
                self.stdout.write(f"✅ Usuário '{user_data['username']}' criado")
            else:
                self.stdout.write(f"ℹ️  Usuário '{user_data['username']}' já existe")
        
        # Criar algumas tarefas de exemplo se não existirem
        if Task.objects.count() == 0:
            self.stdout.write("📋 Criando tarefas de exemplo...")
            
            try:
                pendente = Status.objects.get(name="Pendente")
                andamento = Status.objects.get(name="Em Andamento")
                concluida = Status.objects.get(name="Concluída")
                
                joao = User.objects.get(username="joao")
                maria = User.objects.get(username="maria")
                admin = User.objects.get(username="admin")
                
                tarefas_exemplo = [
                    {
                        'title': 'Implementar sistema de login',
                        'description': 'Desenvolver funcionalidade de autenticação de usuários.',
                        'user': joao,
                        'status': concluida
                    },
                    {
                        'title': 'Criar dashboard administrativo',
                        'description': 'Desenvolver interface para visualizar todas as tarefas.',
                        'user': joao,
                        'status': andamento
                    },
                    {
                        'title': 'Implementar responsividade',
                        'description': 'Adaptar todas as telas para dispositivos móveis.',
                        'user': maria,
                        'status': pendente
                    },
                    {
                        'title': 'Documentar sistema',
                        'description': 'Criar documentação completa do projeto.',
                        'user': admin,
                        'status': andamento
                    }
                ]
                
                for tarefa_data in tarefas_exemplo:
                    Task.objects.create(**tarefa_data)
                    self.stdout.write(f"✅ Tarefa '{tarefa_data['title']}' criada")
                    
            except Exception as e:
                self.stdout.write(f"⚠️  Erro ao criar tarefas: {e}")
        else:
            self.stdout.write("ℹ️  Tarefas já existem no sistema")
        
        # Resumo final
        self.stdout.write("\n" + "="*50)
        self.stdout.write(self.style.SUCCESS("🎉 CONFIGURAÇÃO CONCLUÍDA!"))
        self.stdout.write(f"📊 Total de usuários: {User.objects.count()}")
        self.stdout.write(f"📋 Total de tarefas: {Task.objects.count()}")
        self.stdout.write(f"📈 Total de status: {Status.objects.count()}")
        
        if created_users:
            self.stdout.write("\n🔑 Usuários para login:")
            self.stdout.write("- joao / 123456")
            self.stdout.write("- maria / 123456") 
            self.stdout.write("- admin / admin123")
            
        self.stdout.write("="*50)