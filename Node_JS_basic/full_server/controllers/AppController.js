// full_server/controllers/AppController.js

class AppController {
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}

module.express = AppController;
