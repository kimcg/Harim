/**
 * 1. 천단위 콤마 처리
 * 2. 팝업창 오픈 (중앙)
 * 3. 팝업창 오픈 (중앙) 
 * 4. form 설정 후 팝업 오픈하는 함수 
 * 5. 달력
 * 6. 기간 달력
 * 7. parseInt
 * 8. 객체 여부 반환
 * 9. 공백외의 값 확인
 * 10. 부모창의 아이프레임 사이즈 변경
 */

/**
 * 1. 천단위 콤마 처리
 */
function fn_FormatNumberComma(n) {
	if(n == null){
		return 0;
	}else{
		if(n < 0)
			return "-" + (n * -1).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
		else
			return n.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ",");
	}
}

/**
 * 2. 콤마 지우기
 */
function fn_FormatNumberUnComma(n){
	if(n == null){
		return 0;
	}else{
	    return n.toString().replace(/[^-?\d]+/g, '');
	}
}

/**
 * 3. 팝업창 오픈 (중앙)
 */
function fn_OpenPopup() {
	var args = arguments;
	var name = args[0];
	var url = args[1];
	var width = args[2];
	var height = args[3];
	var scrollbars = args[4]!=null?args[4]:'no';
	
	var leftpos = (screen.availWidth - width) / 2; 
	var toppos = (screen.availHeight - height) / 2; 
	if (!url || url == "") url = "about:blank";
	return window.open(url, name, 'scrollbars='+scrollbars+', toolbar=no, location=no, status=no, menubar=no, resizable=yes, width='+width+', height='+height+', left='+leftpos+', top='+toppos);
}

/**
 * 4. form 설정 후 팝업 오픈하는 함수 
 */
function fn_PopupSubmit()
{
	var args = arguments;
	var form = args[0]==null?"#popupForm":args[0];
	var target = args[1]==null?"popWindow":args[1];
	var action = args[2]==null?"about:blank":args[2];
	var width = args[3]==null?"700":args[3];
	var height = args[4]==null?"450":args[4];
	
	fn_OpenPopup(target, "about:blank", width, height ,'yes');
	
	$(form).attr("target", target);
	$(form).attr("action", action);
	
	$(form).submit();
}

/**
 * 5. 달력
 */
function fn_DatePicker(d){
	$(d).inputmask("yyyy-mm-dd", {"placeholder": "yyyy-mm-dd"});
	$(d).daterangepicker({
		 format: 'YYYY-MM-DD',
		 showDropdowns: true,
		 singleDatePicker: true,
		 locale: {
	          cancelLabel: '취소',
	          applyLabel: '선택',
	      }
 	});
}

/**
 * 6. 기간 달력
 */
function fn_DateRangePicker(r, f, t){
	$(r).daterangepicker({
			 format: 'YYYY-MM-DD',
			 showDropdowns: true,
			 separator : '~',
			 locale: {
		          cancelLabel: '취소',
		          applyLabel: '선택',
		      }
	 });
	
	$(r).on('apply.daterangepicker', function(ev, picker) {
		
		$(f).val(picker.startDate.format("YYYY-MM-DD"));
		$(t).val(picker.endDate.format("YYYY-MM-DD"));
	});
	
	$(r).on('cancel.daterangepicker', function(ev, picker) {
	      $(this).val('');
	      $(f).val('');
	      $(t).val('');
	  });
}

/**
 * 7. parseInt
 */
function parseIntNan(val) {
	val += "";
	val = val.replace(/\,/g,""); // , 제거
	return parseInt(val) || 0;
}

/**
 * 8. 객체 여부 반환
 */
function isObject(obj) {
	if (typeof(obj) == "object") return true;
	return false;
}

/**
 * 9. 공백외의 값 확인
 * @param obj
 * @returns {Boolean}
 */
function isEmpty(obj) {
	var objVal="";
	if (isObject(obj)) {
		objVal = String($(obj).val());
	} else {
		objVal = String(obj);
	}
	
  if (objVal == null || objVal == undefined || objVal == "undefined" || objVal.replace(/ /gi,"") == "" || objVal.replace("　","") == "") {
      return true;
  }

  return false;
}

/**
 * 10. 아이프레임 사이즈 변경
 * parent.getReSize();
 */
function getDocHeight(doc)
{
	var docHt = 0, sh, oh;
	if (doc.height)
	{
		docHt = doc.height;
	}
	else if (doc.body)
	{
		if (doc.body.scrollHeight) docHt = sh = doc.body.scrollHeight;
		if (doc.body.offsetHeight) docHt = oh = doc.body.offsetHeight;
		if (sh && oh) docHt = Math.max(sh, oh);
	}
	return docHt;
}

/**
 * 11. 
 * parent.getReSize();
 */
function getReSize(id)
{
	var iframeWin = window.frames[id];

	var iframeEl = window.document.getElementById? window.document.getElementById(id): document.all? document.all[id]: null;

	if ( iframeEl && iframeWin )
	{
		var docHt = getDocHeight(iframeWin.document);

		if (docHt != iframeEl.style.height) iframeEl.style.height = docHt + 'px';
	}
	else
	{ // firefox
		var docHt = window.document.getElementById(id).contentDocument.height;
		window.document.getElementById(id).style.height = docHt + 'px';
	}
}


/**12 KeyUp 숫자 콤마 찍기
 * @param obj
 */
function fnFormatComma(obj){
	if(!isEmpty(obj)){
		var ojbVal = String($(obj).val()).replace(/[^0-9]/gi, '');
		var rtnVal = Number(ojbVal).toLocaleString();
		$(obj).val(rtnVal);
	}	
}

/**
 * 13 문자열 값 확인
 * @param obj
 * @returns {Boolean}
 */
function isEmptyString(str) {

  if (str == null || str == undefined || str == "undefined" || str.replace(/ /gi,"") == "" || str.replace("　","") == "") {
      return true;
  }

  return false;
}


/**
 * 14 실시간 콤마 찍기
 * 사용볍 : onKeyup="fnSetImdtlComma(this)"
 * @param str
 * @returns {String}
 */
function fnSetImdtlComma(obj) {
	obj.value = fn_FormatNumberComma(fn_FormatNumberUnComma(obj.value));
}

/**
 * 15 브라우저 구분
 * @returns {String}
 */
function fnBrwsrSe() {
	var browser = navigator.userAgent.toLowerCase();
	
	if ( -1 != browser.indexOf('chrome') )
		return 'chrome';
	if ( -1 != browser.indexOf('msie') )
		return 'msie';
	if ( -1 != browser.indexOf('opera') )
		return 'opera';
	if ( -1 != browser.indexOf('mozilla') )
		return 'mozilla';
	
	return 'undefined browser';
}

/**
 * 16 프레임워크 에러체크 - 리턴값 : 정상[true] / 예외 또는 파라미터 값에 문제가 있는경우 [false]
 * @param data, message
 * @returns {Boolean}
 */
function fnFworkErrorCheck()
{
	var args = arguments;
	var data = args[0];
	var message = isEmptyString(args[1])?"처리하지 못했습니다. 관리자에게 문의하세요.":args[1];

	if(typeof data === 'object')
	{
		if(data == null || data == undefined)
		{
			console.log("data[object] : null 또는 undefined 값입니다.");
			return false;
		}
		
		if(data.result == 'error')
		{
			alert(data.message);
			return false;
		}
		else
			return true;
	}
	else if(typeof data === 'string')
	{
		if(isEmptyString(data))
		{
			console.log("data[string] : 문자열값이 공백입니다.");
			return false;
		}

		if(data == 'error')
		{
			alert(message);
			return false;
		}
		else
			return true;
	}
	else
	{
		console.log("파라미터 형식이 object 또는 string이 아닙니다.");
		return false;
	}
}

/**
 * 17 Splitter 설정
 */
function fnDivSplitter(){
	var args = arguments;
	var mOpts = args[0];
	var aOpts = args[1];
	var bOpts = args[2];
	var menuId = args[3];

	if(mOpts.type == 'h') mOpts["sizeTop"] = true;
	var sOpts = $.extend(true,{
		 type : "v"	
	 },mOpts);
	mOpts.css.height = (Number(mOpts.css.height.replace("px", "")) - 20)+"px";		 	
	
	if(aOpts.css.height != undefined){
		aOpts.css["max-height"] = aOpts.css.height;
	}
	if(mOpts.css != undefined) $(mOpts.id).css(mOpts.css);	

	if(menuId != null){
		var boxhegiht = 0;
		$.each(parent.$("#ifrm_"+menuId).contents().find("div.box"), function(){
			boxhegiht += $(this).outerHeight(true);
		});
		
		console.log("inqireDiv :: ", $("#inqireDiv").outerHeight(true));
		console.log("splitter-bar :: ", $(".splitter-bar").outerHeight(true));
		
		
		console.log("windowHeight :: ", $(window).height());
		console.log("iframe height :: " , parent.$("#ifrm_"+menuId).contents().height());
		console.log("iframe body height :: ", parent.$("#ifrm_"+menuId).contents().find("body").outerHeight(true));
		console.log("boxhegiht :: ", boxhegiht);
	}

	
 	var ah, bh, aw, bw;
	if(sOpts.type == 'h'){
		var jqg = $(mOpts.id).find("div[id^=gbox_grid]");
		var dtb = $(mOpts.id).find("div[class^=dataTables_wrapper]");
		if(jqg.length > 0){
			var jqg_id = $(jqg).attr("id").replace(/gbox_/g, "");
			ah = Number($("#"+jqg_id).jqGrid("getGridParam", "height"))+100;
			ah = ah+"px";
			
		}
		if(dtb.length > 0){
			dtb.height();
			//console.log("dtb height :: ", dtb.height());
		}
		//aOpts.css["margin-left"] = "5px";
	}else{
		
	}

	if(aOpts.css != undefined) $(aOpts.id).css(aOpts.css);
	if(bOpts.css != undefined) $(bOpts.id).css(bOpts.css);		
	$(mOpts.id).splitter(sOpts);
	//console.log("$(mOpts.id).splitter().resize() :: ", $(mOpts.id).splitter().resize());
	//parent.$("#ifrm_"+menuId).bind('splitterResize', function(){$(mOpts.id).splitter().resize()});
}


/**
 * Path 가져오기
 */
function getContextPath(){
    var offset=location.href.indexOf(location.host)+location.host.length;
    var ctxPath=location.href.substring(offset,location.href.indexOf('/',offset+1));
    return ctxPath;
}


/**
 * form 전송함수
 */
function ComSubmit() {
	var args = arguments;
	var opt_formId = args[0]==null?"#inqireForm":args[0];
	
	this.formId = opt_formId;
	this.url = "";
	
	/*if(this.formId == "inqireForm"){
		$("#inqireForm")[0].reset();
	}*/
	
	this.setUrl = function setUrl(url){
		this.url = url;
	};
	
	this.addParam = function addParam(key, value){
		$("#"+this.formId).append($("<input type='hidden' name='"+key+"' id='"+key+"' value='"+value+"' >"));
	};
	
	this.submit = function submit(){
		var frm = $("#"+this.formId)[0];
		frm.action = this.url;
		frm.method = "post";
		frm.submit();
	};
}

function time_format(d) {
    var date = new Date();
    hours = date.getHours();
    minutes = date.getMinutes();
    seconds = date.getSeconds();
    var rtn;

    if(d == 'h') rtn = hours;
    else if(d == 'm') rtn = minutes;
    else rtn = seconds;

    return rtn;
}

function format_two_digits(n) {
    return n < 10 ? '0' + n : n;
}


( function( $ ) {
	$( document ).ready(function() {
        $('#cssmenu > ul > li > a').click(function() {
          $('#cssmenu li').removeClass('active');
          $(this).closest('li').addClass('active');
          var checkElement = $(this).next();
          if((checkElement.is('ul')) && (checkElement.is(':visible'))) {
            $(this).closest('li').removeClass('active');
            checkElement.slideUp('normal');
          }
          if((checkElement.is('ul')) && (!checkElement.is(':visible'))) {
            $('#cssmenu ul ul:visible').slideUp('normal');
            checkElement.slideDown('normal');
          }
          if($(this).closest('li').find('ul').children().length == 0) {
            return true;
          } else {
            return false;
          }
        });
	});
	} )( jQuery );