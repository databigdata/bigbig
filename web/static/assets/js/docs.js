jQuery(function(){
  // Track downloads
  $('#download-master').click(function(){
    _trackEvent('Downloads', 'master');
  });
});

jQuery(document).ready(function($) {

  /* Docs scrollspy */
  $('body').scrollspy({
    target: '.bs-sidebar',
    offset: 0
  })

  $(window).on('load', function () {
    $('body').scrollspy('refresh')
  })

  // back to top
  setTimeout(function () {
    var $sideBar = $('.bs-sidebar')

    $sideBar.affix({
      offset: {
        top: function () {
          var offsetTop      = $sideBar.offset().top
          var sideBarMargin  = parseInt($sideBar.children(0).css('margin-top'), 10)

          return (this.top = offsetTop - sideBarMargin)
        }
      , bottom: function () {
          return (this.bottom = $('.bs-footer').outerHeight(true))
        }
      }
    })
  }, 100)

  /* Run examples */
  $('.token-example-field').tokenfield();

  $('#tokenfield-1').tokenfield({
    autocomplete: {
      source: ['후천성면역결핍증식',
'후두암식',
'화상식',
'협심증식',
'허혈성심장질환식',
'프라더 윌리 증후군식',
'폐렴식',
'폐경기 및 여성의 갱년기',
'페닐케톤뇨증, PKU',
'패혈증식',
'크론병식',
'콜레라식',
'췌장암식',
'지방간식',
'제대혈조혈모세포식',
'전이성간암식',
'전립암식',
'저혈압식',
'저혈당증식',
'저칼륨식',
'저마그네슘혈증식',
'저나트륨혈증식',
'장폐색식, 또는 장유착식',
'자궁내 성장지연식',
'자궁경부암식',
'임신성고혈압식',
'임신성 당뇨식',
'유방암식',
'윌슨병식',
'위암식',
'위식도역류질환식',
'위궤양식',
'열량조절식',
'알콜성간질환식',
'십이지장궤양식',
'심근경색식',
'신증후군식',
'식중독식',
'식도정맥류식',
'식도염식',
'식도암식',
'셀리악병식',
'섭식장애식',
'사구체신염식',
'빈혈식',
'복막염식',
'변비식',
'바이러스성 간염식',
'말기신질환식',
'만성신부전식',
'만성담낭염식',
'만성 췌장염식',
'덤핑증후군식',
'만성신부전식',
'말기신질환식',
'대장암식',
'대사증후군식',
'당원병식/당원축적병식',
'당뇨병식',
'담낭암식',
'단장증후군식',
'급성췌장염식',
'급성신부전식',
'구루병식',
'골다공증식',
'고혈압식 / 폐성 고혈압식',
'고지혈증식',
'갑상선암식',
'갑상선기능항진증',
'갑상선기능저하증',
'간이식후식',
'간성혼수식',
'간경화식',
'각기병식'],
      delay: 100
    },
    showAutocompleteOnFocus: true,
    delimiter: [',',' ', '-', '_']
  });

  var engine = new Bloodhound({
    local: [{value: '후천성면역결핍증식'},
{value: '후두암식'},
{value: '화상식'},
{value: '협심증식'},
{value: '허혈성심장질환식'},
{value: '프라더 윌리 증후군식'},
{value: '폐렴식'},
{value: '폐경기 및 여성의 갱년기'},
{value: '페닐케톤뇨증, PKU'},
{value: '패혈증식'},
{value: '크론병식'},
{value: '콜레라식'},
{value: '췌장암식'},
{value: '지방간식'},
{value: '제대혈조혈모세포식'},
{value: '전이성간암식'},
{value: '전립암식'},
{value: '저혈압식'},
{value: '저혈당증식'},
{value: '저칼륨식'},
{value: '저마그네슘혈증식'},
{value: '저나트륨혈증식'},
{value: '장폐색식, 또는 장유착식'},
{value: '자궁내 성장지연식'},
{value: '자궁경부암식'},
{value: '임신성고혈압식'},
{value: '임신성 당뇨식'},
{value: '유방암식'},
{value: '윌슨병식'},
{value: '위암식'},
{value: '위식도역류질환식'},
{value: '위궤양식'},
{value: '열량조절식'},
{value: '알콜성간질환식'},
{value: '십이지장궤양식'},
{value: '심근경색식'},
{value: '신증후군식'},
{value: '식중독식'},
{value: '식도정맥류식'},
{value: '식도염식'},
{value: '식도암식'},
{value: '셀리악병식'},
{value: '섭식장애식'},
{value: '사구체신염식'},
{value: '빈혈식'},
{value: '복막염식'},
{value: '변비식'},
{value: '바이러스성 간염식'},
{value: '말기신질환식'},
{value: '만성신부전식'},
{value: '만성담낭염식'},
{value: '만성 췌장염식'},
{value: '덤핑증후군식'},
{value: '만성신부전식'},
{value: '말기신질환식'},
{value: '대장암식'},
{value: '대사증후군식'},
{value: '당원병식/당원축적병식'},
{value: '당뇨병식'},
{value: '담낭암식'},
{value: '단장증후군식'},
{value: '급성췌장염식'},
{value: '급성신부전식'},
{value: '구루병식'},
{value: '골다공증식'},
{value: '고혈압식 / 폐성 고혈압식'},
{value: '고지혈증식'},
{value: '갑상선암식'},
{value: '갑상선기능항진증'},
{value: '갑상선기능저하증'},
{value: '간이식후식'},
{value: '간성혼수식'},
{value: '간경화식'},
{value: '각기병식'}],
    datumTokenizer: function(d) {
      return Bloodhound.tokenizers.whitespace(d.value);
    },
    queryTokenizer: Bloodhound.tokenizers.whitespace
  });
  engine.initialize();

  $('#tokenfield-typeahead').tokenfield({
    typeahead: [null, { source: engine.ttAdapter() }]
  });

  $('#tokenfield-2')
    .on('tokenfield:createtoken', function (e) {
      var data = e.attrs.value.split('|')
      e.attrs.value = data[1] || data[0]
      e.attrs.label = data[1] ? data[0] + ' (' + data[1] + ')' : data[0]
    })
    .on('tokenfield:createdtoken', function (e) {
      // Über-simplistic e-mail validation
      var re = /\S+@\S+\.\S+/
      var valid = re.test(e.attrs.value)
      if (!valid) {
        $(e.relatedTarget).addClass('invalid')
      }
    })
    .on('tokenfield:edittoken', function (e) {
      if (e.attrs.label !== e.attrs.value) {
        var label = e.attrs.label.split(' (')
        e.attrs.value = label[0] + '|' + e.attrs.value
      }
    })
    .on('tokenfield:removedtoken', function (e) {
      if (e.attrs.length > 1) {
        var values = $.map(e.attrs, function (attrs) { return attrs.value });
        alert(e.attrs.length + ' tokens removed! Token values were: ' + values.join(', '))
      } else {
        alert('Token removed! Token value was: ' + e.attrs.value)
      }
    })
    .tokenfield()

});