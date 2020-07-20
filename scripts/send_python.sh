apt install -y zip
zip -r visitor_count.zip sources/visitor_count
gsutil cp visitor_count.zip gs://coffeetime-dev-cloudresume-functions