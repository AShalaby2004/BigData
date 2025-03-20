CONTAINER_NAME="bd-a1-container"

mkdir -p bd-a1/service-result

docker cp $CONTAINER_NAME:/home/doc-bd-a1/res_dpre.csv bd-a1/service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-1.txt bd-a1/service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-2.txt bd-a1/service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/eda-in-3.txt bd-a1/service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/vis.png bd-a1/service-result/
docker cp $CONTAINER_NAME:/home/doc-bd-a1/k.txt bd-a1/service-result/

docker stop $CONTAINER_NAME

echo "All results copied to bd-a1/service-result/ and container stopped."