 Elasticsearch security features have been automatically configured!
-> Authentication is enabled and cluster connections are encrypted.

->  Password for the elastic user (reset with `bin/elasticsearch-reset-password -u elastic`):
  6o_WW5r2hUkFGXbXIOq2

->  HTTP CA certificate SHA-256 fingerprint:
  334a7805e5aa202e5fd69798b8a83cc1ab86e4a562b6707b7dac74d56af29328

->  Configure Kibana to use this cluster:
* Run Kibana and click the configuration link in the terminal when Kibana starts.
* Copy the following enrollment token and paste it into Kibana in your browser (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjIuMyIsImFkciI6WyIxOTIuMTY4LjMyLjI6OTIwMCJdLCJmZ3IiOiIzMzRhNzgwNWU1YWEyMDJlNWZkNjk3OThiOGE4M2NjMWFiODZlNGE1NjJiNjcwN2I3ZGFjNzRkNTZhZjI5MzI4Iiwia2V5IjoiNDlMRWJJRUJfZlY4SXowYkp2UlE6TTdENnloLWxRc0tQSjUtQXJnWkIzdyJ9

-> Configure other nodes to join this cluster:
* Copy the following enrollment token and start new Elasticsearch nodes with `bin/elasticsearch --enrollment-token <token>` (valid for the next 30 minutes):
  eyJ2ZXIiOiI4LjIuMyIsImFkciI6WyIxOTIuMTY4LjMyLjI6OTIwMCJdLCJmZ3IiOiIzMzRhNzgwNWU1YWEyMDJlNWZkNjk3OThiOGE4M2NjMWFiODZlNGE1NjJiNjcwN2I3ZGFjNzRkNTZhZjI5MzI4Iiwia2V5IjoiNU5MRWJJRUJfZlY4SXowYkp2UlE6VGdEOEZkZmRST3V2OUtXamZpdnBIZyJ9

  If you're running in Docker, copy the enrollment token and run:
  `docker run -e "ENROLLMENT_TOKEN=<token>" docker.elastic.co/elasticsearch/elasticsearch:8.2.3`