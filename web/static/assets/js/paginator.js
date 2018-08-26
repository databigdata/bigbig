
    function getStartedInitialization(){
        var options = {
            currentPage: 3,
            totalPages: 10
        }

        $('#bp-get-started-initialization').bootstrapPaginator(options);
    }

    function minimumConfiguration(){
        var options = {
            currentPage: 3,
            totalPages: 10
        }

        $('#bp-example-initialization').bootstrapPaginator(options);
    }

    function sizeAndAlignment() {

        var options = {
                currentPage: 3,
                totalPages: 10,
                size:"normal",
                alignment:"left"
            },
            container = $('#bp-example-size-alignment')



        container.bootstrapPaginator(options);

        function changeContainerSize(size){
            options.size = size;

            container.bootstrapPaginator(options);
        }

        $('#bp-size-mini').click(function(){

            changeContainerSize("mini")

            updateCode()
        })

        $('#bp-size-small').click(function(){

            changeContainerSize("small")

            updateCode()
        })

        $('#bp-size-normal').click(function(){

            changeContainerSize("normal")

            updateCode()
        })

        $('#bp-size-large').click(function(){

            changeContainerSize("large")

            updateCode()
        })

        function changeContainerAlignment(alignment){
            options.alignment = alignment;

            container.bootstrapPaginator(options);
        }

        $("#bp-alignment-left").click(function(){

            changeContainerAlignment("left");

            updateCode()
        })

        $("#bp-alignment-center").click(function(){

            changeContainerAlignment("center");

            updateCode()
        })

        $("#bp-alignment-right").click(function(){

            changeContainerAlignment("right");

            updateCode()

        })

        function updateCode()
        {
            $('#bp-size-alignment-code').empty();

            var str = "\r\n\
        var options = {\r\n\
                currentPage: 3,\r\n\
                totalPages: 10,\r\n\
                size:'"+options.size+"',\r\n\
                alignment:'"+options.alignment+"'\r\n\
            }\r\n\r\n\
        $('#example').bootstrapPaginator(options);\r\n        ";



            var text = hljs.highlight("javascript", str)

            $('#bp-size-alignment-code').html(text.value)
        }

    }

    function pageItemText(){

        var options = {
            currentPage: 3,
            totalPages: 10,
            itemTexts: function (type, page, current) {
                switch (type) {
                    case "first":
                        return "First";
                    case "prev":
                        return "Previous";
                    case "next":
                        return "Next";
                    case "last":
                        return "Last";
                    case "page":
                        return (page == current)?"*p"+page:"p"+page;
                }
            }
        }

        $('#bp-example-page-item-text').bootstrapPaginator(options);

    }

    function pageItemTooltipText(){
        var options = {
            currentPage: 3,
            totalPages: 10,
            tooltipTitles: function (type, page, current) {
                switch (type) {
                    case "first":
                        return "Tooltip for first page";
                    case "prev":
                        return "Tooltip for previous page";
                    case "next":
                        return "Tooltip for next page";
                    case "last":
                        return "Tooltip for last page";
                    case "page":
                        return "Tooltip for page " + page;
                }
            }
        }

        $('#bp-example-page-item-tooltip-text').bootstrapPaginator(options);
    }

    function useBootstrapTooltip(){

        var options = {
            currentPage: 3,
            totalPages: 10,
            useBootstrapTooltip:true
         }

        $('#bp-example-page-item-use-bootstrap-tooltip').bootstrapPaginator(options);

    }

    function bootstrapTooltipConfiguration(){

        var options = {
            currentPage: 3,
            totalPages: 10,
            useBootstrapTooltip:true,
            tooltipTitles: function (type, page, current) {
                switch (type) {
                    case "first":
                        return "Go To First Page <i class='icon-fast-backward icon-white'></i>";
                    case "prev":
                        return "Go To Previous Page <i class='icon-backward icon-white'></i>";
                    case "next":
                        return "Go To Next Page <i class='icon-forward icon-white'></i>";
                    case "last":
                        return "Go To Last Page <i class='icon-fast-forward icon-white'></i>";
                    case "page":
                        return "Go to page " + page + " <i class='icon-file icon-white'></i>";
                }
            },
            bootstrapTooltipOptions: {
                html: true,
                placement: 'bottom'
            }
        }

        $('#bp-example-page-item-bootstrap-tooltip-configuration').bootstrapPaginator(options);

    }

    function itemContainerClassDemo(){
        var options = {
            currentPage: 3,
            totalPages: 10,
            itemContainerClass: function (type, page, current) {
                return (page === current) ? "active" : "pointer-cursor";
            }
        }

        $('#bp-example-page-item-container-class').bootstrapPaginator(options);
    }

    function numberOfPagesDemo(){

        var options = {
            currentPage: 2,
            totalPages: 10,
            numberOfPages:3
        }

        $('#bp-example-number-of-pages').bootstrapPaginator(options);
    }

    function pageUrlDemo(){

        var options = {
            currentPage: 3,
            totalPages: 10,
            pageUrl: function(type, page, current){

                return "http://example.com/list/page/"+page;

            },
            onPageClicked:function(e,originalEvent,type,page){
                originalEvent.preventDefault();
                originalEvent.stopPropagation();

                var target = originalEvent.currentTarget;

                var url = $(target).attr("href");

                $("#page-url-alert-content").text("Page item url: "+url)
            }
        }

        $('#bp-example-page-url').bootstrapPaginator(options);
    }

    function presenceOfPageDemo(){

        var options = {
            currentPage: 3,
            totalPages: 10,
            shouldShowPage:function(type, page, current){
                switch(type)
                {
                    case "first":
                    case "last":
                        return false;
                    default:
                        return true;
                }
            }
        }

        $('#bp-example-presence-of-page').bootstrapPaginator(options);
    }

    function pageClickedEvent()
    {
        var options = {
            currentPage: 3,
            totalPages: 10,
            onPageClicked: function(e,originalEvent,type,page){
                $('#page-clicked-alert-content').text("Page item clicked, type: "+type+", page: "+page);
            }
        }

        $('#bp-example-page-clicked-event').bootstrapPaginator(options);
    }

    function pageClickedEventStoppable()
    {
        var options = {
            currentPage: 3,
            totalPages: 10,
            onPageClicked: function(e,originalEvent,type,page){
                e.stopImmediatePropagation();

                var currentTarget = $(e.currentTarget);

                var pages = currentTarget.bootstrapPaginator("getPages");

                $('#page-clicked-alert-content-stoppable').text("Page item clicked, current page: "+pages.current);

                setTimeout(function(){

                    currentTarget.bootstrapPaginator("show",page);

                    var pages = currentTarget.bootstrapPaginator("getPages");

                    $('#page-clicked-alert-content-stoppable').append("<br/>Page item click finished, current page: "+pages.current);

                },3000);

            }
        }

        $('#bp-example-page-clicked-event-stoppable').bootstrapPaginator(options);
    }

    function pageChangedEvent()
    {
        var options = {
            currentPage: 3,
            totalPages: 10,
            onPageChanged: function(e,oldPage,newPage){
                $('#page-changed-alert-content').text("Current page changed, old: "+oldPage+", new: "+newPage);
            }
        }

        $('#bp-example-page-changed-event').bootstrapPaginator(options);

        $('#page-changed-select').change(function(){
            var page = $(this).val();

            $('#bp-example-page-changed-event').bootstrapPaginator("show",page);
        })
    }

    function showFunctionDemo(){

        var options = {
            currentPage: 3,
            totalPages: 10
        }

        $('#bp-example-show-function').bootstrapPaginator(options);

        function updateCode(fname,page){

            var fstr = "\""+fname+"\""+(fname=="show"?", "+page:"")

            var str = "\r\n\
        var options = {\r\n\
                currentPage: 3,\r\n\
                totalPages: 10,\r\n\
            }\r\n\r\n\
        $('#bp-example-size-alignment').bootstrapPaginator(options);\r\n\r\n\
        $('#bp-example-size-alignment').bootstrapPaginator("+fstr+");\r\n        ";



            var text = hljs.highlight("javascript", str)

            $('#show-function-code').html(text.value)
        }

        function updateButtonStatus(){
            var pages = $('#bp-example-show-function').bootstrapPaginator("getPages");

            if(pages.first)
            {
                $('#bp-example-show-first-btn').removeClass("disabled")
            }else
            {
                $('#bp-example-show-first-btn').addClass("disabled")
            }

            if(pages.prev)
            {
                $('#bp-example-show-prev-btn').removeClass("disabled")
            }else
            {
                $('#bp-example-show-prev-btn').addClass("disabled")
            }

            if(pages.next)
            {
                $('#bp-example-show-next-btn').removeClass("disabled")
            }else
            {
                $('#bp-example-show-next-btn').addClass("disabled")
            }

            if(pages.last)
            {
                $('#bp-example-show-last-btn').removeClass("disabled")
            }else
            {
                $('#bp-example-show-last-btn').addClass("disabled")
            }


        }

        $('#show-page-select').change(function (){

            var page = $(this).val();

            $('#bp-example-show-function').bootstrapPaginator("show",page);

            updateButtonStatus();

            updateCode("show",page);

        })

        $('#bp-example-show-first-btn').click(function(){

            $('#bp-example-show-function').bootstrapPaginator("showFirst");

            updateButtonStatus();

            updateCode("showFirst");

        })

        $('#bp-example-show-prev-btn').click(function(){

            $('#bp-example-show-function').bootstrapPaginator("showPrevious");

            updateButtonStatus();

            updateCode("showPrevious");

        })

        $('#bp-example-show-next-btn').click(function(){

            $('#bp-example-show-function').bootstrapPaginator("showNext");

            updateButtonStatus();

            updateCode("showNext");

        })

        $('#bp-example-show-last-btn').click(function(){

            $('#bp-example-show-function').bootstrapPaginator("showLast");

            updateButtonStatus();

            updateCode("showLast");

        })

    }

    function getPagesFunctionDemo(){

        var options = {
            currentPage: 3,
            totalPages: 10
        }

        $('#bp-example-get-pages-function').bootstrapPaginator(options);

        updateCode();

        $('#bp-example-get-pages-btn').click(function(){
            updateCode();
        })


        function updateCode()
        {
            var codeSection = $('#get-pages-code');

            codeSection.empty();

            var pages = $('#bp-example-get-pages-function').bootstrapPaginator("getPages");

            var pagesStr = "[";

            for(var i = 0;i < pages.length;i++)
            {
                pagesStr += (i < pages.length-1)?pages[i]+", ":pages[i]+"]"
            }



            var str = "\r\n\
        //numeric pages array    \r\n\
        "+pagesStr+"\r\n\r\n\
        //additional attributes\r\n\
        {\r\n\
            first: "+pages.first+",\r\n\
            prev: "+pages.prev+",\r\n\
            next: "+pages.next+",\r\n\
            last: "+pages.last+"\r\n\
            current: "+pages.current+"\r\n\
            total: "+pages.total+"\r\n\
            numberOfPages: "+pages.numberOfPages+"\r\n\
        }\r\n\r\n\
        \r\n        ";



            var text = hljs.highlight("javascript", str)

            codeSection.html(text.value)
        }


    }

    function setOptionsFunctionDemo(){
        //  bp-exmaple-set-option-update-btn

        var options = {
            currentPage: 3,
            totalPages: 10
        }

        $('#bp-example-set-options-function').bootstrapPaginator(options);

        updateCode();

        $("#bp-exmaple-set-option-update-btn").click(function(){
            updateCode();
        })

        function updateCode(){

            var numberOfPages = $('#bp-example-set-option-number-of-page-select').val(),
                totalPages = $('#bp-example-set-option-total-pages-select').val()

            var str = "\r\n\
        var options = {\r\n\
                currentPage: 3,\r\n\
                totalPages: 10,\r\n\
            }\r\n\r\n\
        $('#example').bootstrapPaginator(options);\r\n\r\n\
        options = {\r\n\
                currentPage: "+numberOfPages+",\r\n\
                totalPages: "+totalPages+",\r\n\
            }\r\n\r\n\
        $('#example').bootstrapPaginator(options);\r\n        ";


            $('#bp-example-set-options-function').bootstrapPaginator({
                numberOfPages: numberOfPages,
                totalPages: totalPages
            });

            var text = hljs.highlight("javascript", str)

            $('#set-option-code').html(text.value)

        }

    }

    $(function(){
        getStartedInitialization();
        minimumConfiguration();
        sizeAndAlignment();
        pageItemText();
        pageItemTooltipText();
        useBootstrapTooltip();
        bootstrapTooltipConfiguration();
        itemContainerClassDemo();
        numberOfPagesDemo();
        pageUrlDemo();
        presenceOfPageDemo();
        pageClickedEvent();
        pageClickedEventStoppable();
        pageChangedEvent();
        showFunctionDemo();
        getPagesFunctionDemo();
        setOptionsFunctionDemo();

        $('#navbar').scrollspy({offset:100})

        $("a[href^='#']").click(function(e){
            e.preventDefault();


            var href = $(this).attr("href"),
                id = href.substr(href.indexOf('#')),
                item = $(id);

            if(!item || item.length < 1)
            {
                return;
            }

            var  position = item.position(),
                 top = position.top;

            console.log(window.location.pathname)

            History.replaceState({state:3},"State 3",window.location.pathname+id)

            $('body').animate({scrollTop:top-50}, 1000)
        })

    })

    $(document).ready(function() {
        $('pre').each(function(i, e) {
            hljs.highlightBlock(e)
        });

    });
