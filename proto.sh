# protoc --proto_path=. --java_out=java --grpc_java_out=java vandal.proto
PROTO_COMMAND_OUTPUT=$(./manage.py proto)
echo $PROTO_COMMAND_OUTPUT
python -m grpc_tools.protoc -I vandal/proto --python_out=vandal/proto --grpc_python_out=vandal/proto vandal.proto
protoc -I vandal/proto vandal/proto/vandal.proto --go_out=plugins=grpc:vandal/proto/
grpc_tools_node_protoc -I vandal/proto/ --js_out=import_style=commonjs,binary:vandal/proto/ --grpc_out=vandal/proto/ --plugin=protoc-gen-grpc=`which grpc_tools_node_protoc_plugin` vandal/proto/vandal.proto
sed -i 's/import vandal_pb2 as vandal__pb2/import vandal.proto.vandal_pb2 as vandal__pb2/g' vandal/proto/vandal_pb2.py vandal/proto/vandal_pb2_grpc.py
grep -q -F 'exports.grpc = grpc;' vandal/proto/vandal_grpc_pb.js || echo 'exports.grpc = grpc;' >> vandal/proto/vandal_grpc_pb.js
