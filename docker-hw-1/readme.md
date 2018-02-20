Для запуска "серверной" части в корне нужно выполнить:
sudo docker-compose up -d 
Для перекомпиляции добавить --build

Для сборки образа producer в соответствующей папке выполнить:
sudo docker image build -t rabbit-producer .

Для запуска producer:
sudo docker run -it --name producer --rm --network=dockerhw1_backend rabbit-producer


Для чтения из базы предлагается использовать tester:

Сборка образа:
sudo docker image build -t rabbit-tester .

Запуск tester:
sudo docker run -it --name tester --rm --network=dockerhw1_backend rabbit-tester
