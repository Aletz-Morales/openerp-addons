Aloha.ready(function() {
    // Init headless webclient
    // TODO: Webclient research : use iframe embedding mode
    //       Meanwhile, let's HACK !!!
    var $web = $('<div style="display: none;"/>').appendTo('body');
    var $web = $('<div style="display: none;"/>').appendTo($web);
    var s = new openerp.init(['web', 'website']);
    s.web.WebClient.bind_hashchange = s.web.blockUI = s.web.unblockUI = function() {};
    s.web.WebClient.include({ do_push_state: function() {} });
    var wc = new s.web.WebClient();
    wc.appendTo($web);
    var instance = openerp.instances[wc.session.name];
    // Another hack since we have no callback when webclient has loaded modules.
    instance.web.qweb.add_template('/website/static/src/xml/website.xml');

    $(function() {
        var editor = new instance.website.EditorBar(instance.webclient);
        editor.prependTo($('body'));
        $('body').css('padding-top', editor.$el.outerHeight());
    });
});
