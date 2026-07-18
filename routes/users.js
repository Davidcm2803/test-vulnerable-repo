const express = require("express");
const router = express.Router();
const db = require("../utils/db");

// sql injection
router.get("/users/:id", (req, res) => {
  const id = req.params.id;
  const query = "SELECT * FROM users WHERE id = " + id;
  db.query(query, (err, rows) => {
    res.json(rows);
  });
});

// log de credenciales
router.post("/login", (req, res) => {
  console.log("Login attempt: " + req.body.username + " / " + req.body.password);
  res.json({ ok: true });
});

module.exports = router;
