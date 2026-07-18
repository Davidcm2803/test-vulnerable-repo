const express = require("express");
const router = express.Router();

// xss reflejado
router.get("/search", (req, res) => {
  const q = req.query.q;
  res.send("<h1>Resultados para: " + q + "</h1>");
});

// eval con input externo
router.post("/calc", (req, res) => {
  const result = eval(req.body.expression);
  res.json({ result });
});

// cors abierto
router.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  next();
});

module.exports = router;
