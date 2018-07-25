var messages = require('./garuda_pb');
var services = require('./garuda_grpc_pb');

var grpc = require('grpc');

function main() {
  var client = new services.GarudaClient(
    'localhost:50051', grpc.credentials.createInsecure());
  var article = new messages.Article()
  article.setTitle('Article from node-client');
  client.createArticle(article, function(err, article) {
    console.log(err)
    console.log('Article ID:', article.getId());
  });
}

main();
