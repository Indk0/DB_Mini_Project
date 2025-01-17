tasks:
  - init: |
      # Update and install MySQL Server and Client
      sudo apt-get update && sudo apt-get install -y mysql-server mysql-client

      # Create a persistent data directory
      mkdir -p mysql-data

      # Initialize MySQL if it's not already initialized
      if [ ! -d "mysql-data/mysql" ]; then
        sudo mysqld --initialize-insecure --datadir=/workspace/mysql-data
      fi

      # Start MySQL using the persistent data directory
      sudo mysqld --datadir=mysql-data --socket=/tmp/mysql.sock &

      # Wait for MySQL to start
      sleep 5

      # Create a root user password (if needed)
      sudo mysql -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'root'; FLUSH PRIVILEGES;"
