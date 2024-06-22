require 'rake'

# Define your Jekyll build task
desc "Build the Jekyll site"
task :build do
  sh "bundle exec jekyll build"
end

# Define your Jekyll serve task
desc "Serve the Jekyll site locally"
task :serve do
  sh "bundle exec jekyll serve"
end

# Define your Jekyll test task (using html-proofer as an example)
desc "Test the Jekyll site"
task :test do
  sh "bundle exec jekyll build"
  sh "bundle exec htmlproofer ./_site --check-html --allow-hash-href --disable-external"
end
