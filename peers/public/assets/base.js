/* special functions */
String.prototype.trim = function() {return (this.replace(/^[\s\xA0]+/, "").replace(/[\s\xA0]+$/, ""))}
String.prototype.startsWith = function(str) {return (this.match("^"+str)==str)}

function update_feeds() {
    /* referral feed */
    $("section h2").text("REFERRAL");
    load_feed("http://rss.news.yahoo.com/rss/topstories", $("section articles"), 1);
    /* news feed */
    $("aside h2").text("NEWS");
//    load_feed("http://earthquake.usgs.gov/earthquakes/catalogs/1day-M2.5.xml", $("aside articles"));
    load_feed("topstories.xml", $("aside articles"));
    return 1;
}

function load_feed(url,loc,pre) {
    var data=null;
    if (!pre) {pre=0;}
    if (url.startsWith('http://')) {
        $.jGFeed(url,
            function(feed) {
                if(!feed) {
                    add_note("error",url+" fail");
                    return null;
                }
                data = feed;
                if (process_feed(feed,loc,pre)) {
                    add_note("info",url+" successfully loaded");
                }
            },
            5
        );
    } else {
        $.getFeed({
            url: url,
            success: function(feed) {
                data = feed;
                if (process_feed(feed,loc,pre)) {
                    add_note("info",url+" successfully loaded");
                }
            }
        });
    }
    return data;
}

function process_feed(feed,loc,pre) {
    var items = feed.items;
    if (!items) {
        items = feed.entries;
    }
    for (var i=0;i<items.length;i++) {
        var entry = items[i];
        if (pre==1) {
            loc.prepend(update_feed(entry));
        } else {
            loc.append(update_feed(entry));
        }
    }
    return 1;
}

function update_feed(it) {
    var ar,he,su,ti,di;
    var desc = it.content;
    var date = it.publishedDate;
    var max_len = 10000;
    /* processing */
    if (!desc) {desc=it.description;}
    if (!date) {date=it.updated;}
    if (desc.length>max_len) {
        desc = desc.slice(0,max_len) + " ...";
    }
    /* add author */
    he = $("<h3>");
    he.addClass("author");
    he.text(it.title);
    /* add summary */
    su = $("<a>");
    su.addClass("summary");
    su.attr("href","#");
    su.html(desc);
    su.click(select_article);
    /* add footer */
    ti = $("<time>");
    ti.addClass("timeago");
    ti.attr("data-timestamp",date);
    ti.cuteTime();
    /* add to article */
    ar = $("<article>");
    ar.append(he);
    ar.append(su);
    ar.append(ti);
    ar.attr("id", it.title);
    return ar;
}

function select_article(event) {
    var c = $(this).parent();
    var p = $(this).parents().get(2);
    var test = null;
    clear_notes();
    switch(p.tagName.toLowerCase()) {
        case "aside":
            test = "a";
            break;
        case "section":
            test = "b";
            break;
        default:
            return 1;
    }
    $.ajax({
        type:   "POST",
        url:    "http://127.0.0.1:5000/messages/create",
        data:   ({
                    name:       "John",
                    contact:    "639171234567",
                    headers:    "hello:world\ntesting : new",
                    body:       c.attr("id")
                }),
        success: function(data){
                    alert(data);
                }
    });
    add_note("warn",c.attr("id"));
    return 0;
}

function clear_notes() {
    $("notes").empty();
    return 1;
}

function add_note(type,data) {
    /* type is either info, warn, or error */
    var no = $("<h3>");
    no.addClass(type);
    no.text(data);
    $("notes").append(no);
    return 1;
}

function update_css() {
    if ($(window).width() > 1000) {
        $("section").css("width", "69%");
        $("aside").css("width", "29.5%");
        $("aside").css("float", "right");
    } else {
        $("section").css("width", "auto");
        $("aside").css("width", "auto");
        $("aside").css("float", "left");
    }
    return 1;
}

$(document).ready(function(){
    update_feeds();
    update_css();
    $(window).bind("resize", update_css);
    $.fn.cuteTime.settings.refresh=60000; // refresh every minute
});
