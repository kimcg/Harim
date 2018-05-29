function fn_FormClear(frm) {
	var elems = $(frm).find('input, select, textarea, hidden');

	$(frm).get(0).reset();

	$.each(elems, function() {
		if (this.type == "hidden") {

			if(this.name != "STATUS")
				this.value = "";

			// 중복확인 FormClear 시 색깔 처리
			if(this.id == "dplctCheckResult")
			{
				this.value = "N";
				$(this).prev().addClass("dplctCheckResult_bass");
			}

		}
	});
	var sourceElems = $(frm).find('select');
	if(sourceElems.length > 0){
		$.each(sourceElems, function() {
			$("#"+this.name+" option:eq(0)").attr("selected", "selected");
		});
	}

	return elems;
}

function fn_FormSave() {
	var args = arguments; // Parameters
	var saveUrl = args[0];
	var savefrm = args[1];
	var callbackFunction = args[2];

	if(savefrm == null)
		return;

	var elems = $(savefrm).find('input, select, textarea, hidden');

	// 필수값 체크 후 데이터가 없는 경우 true, 있는경우 false
	var essntlFlag = false;

	var saveObj = new Object();
	var saveData = new Array();

	$.each(elems, function() {

		if($(this).attr("essntl") == "true"){
			if($(this).val() == "" || $(this).val() == null || $(this).val() == undefined)
			{
				essntlFlag = true;
				$(this).addClass("essntl_failr");
				return;
			}
			else
			{
				$(this).removeClass("essntl_failr");
			}
		}

	    if(this.type == 'radio'){
	    	$(this).each(function(){
	    	     if($(this).prop('checked')){
	    	    	 saveObj[this.name] = $(this).val();
	    	      }
	    	 });
		}
	    else if(this.type == 'checkbox'){
			if($(this).is(":checked")){
				this.value = 'Y';
			}else{
				this.value = 'N';
			}
			saveObj[this.name] = this.value;
		}
	    else if(this.type == "text"){
			if($(this).attr("bindType") == "amount"){
				this.value = fn_FormatNumberUnComma(this.value);
				saveObj[this.name] = this.value;
			}else{
				saveObj[this.name] = this.value;
			}
		}
	    else{
	    	saveObj[this.name] = this.value;
	    }

	});

	saveData[0] = saveObj;
	var json = JSON.stringify(saveData);

	$.ajax({
		method: "POST"
		, dataType : "json"
		, url: saveUrl
		, data: {"createdRows": json}
		, success: function(data) {
			alert(data.message);
            if (callbackFunction != null
                    && callbackFunction != undefined) {
                callbackFunction(data);
            }
        }
		,error: function() {
            alert('통신장애로 데이터가 처리 되지않았습니다.');
        }
	});
}