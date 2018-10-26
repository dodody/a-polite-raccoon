const express = require('express');
const router = express.Router();
const PythonShell = require('python-shell').PythonShell;

const bodyParser = require('body-parser');
const html = require('html');

router.use(bodyParser.urlencoded({
   extended : true
}));
router.use(bodyParser.json());

router.get('/', function(req, res, next) {
  res.render('index');
 });
 
router.post('/', async(req,res)=>{
	let inputText = req.body.text_box;
	
	// res.send({data: "성공!"});
	//  return;
	 
	if(!inputText){
		res.status(400).send({
			message:"Null value"
		});
	}else{
		PythonShell.run('test.py',{args:[inputText]},(err, results)=> {

	    	if (err) throw err;
	    	else{
	    		res.status(201, {'Content-Type':'text/plain; charset=utf-8'}).send({
	    			data:results[0]
	    		})  		
	    	}
		});
	}
});

module.exports = router;
