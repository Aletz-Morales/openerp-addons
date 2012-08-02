/*---------------------------------------------------------
 * OpenERP web_linkedin (module)
 *---------------------------------------------------------*/

openerp.web_linkedin = function(instance) {
    var QWeb = instance.web.qweb;
    var _t = instance.web._t;
    
    instance.web_linkedin.LinkedinTester = instance.web.Class.extend({
        init: function() {
            this.api_key = "cxnr0l53n73x";
            this.linkedin_added = false;
            this.linkedin_def = $.Deferred();
        },
        test_linkedin: function() {
            var self = this;
            return this.test_api_key().pipe(function() {
                if (self.linkedin_added)
                    return self.linkedin_def.promise();
                var tag = document.createElement('script');
                tag.type = 'text/javascript';
                tag.src = "http://platform.linkedin.com/in.js";
                tag.innerHTML = 'api_key : ' + self.api_key + '\nauthorize : true';
                document.getElementsByTagName('head')[0].appendChild(tag);
                self.linkedin_added = true;
                $(tag).load(function() {
                    self.linkedin_def.resolve();
                });
                return self.linkedin_def.promise();
            });
        },
        test_api_key: function() {
            if (this.api_key) {
                return $.when();
            }
            return new instance.web.Model("ir.config_parameter").call("get_param", ["web.linkedin.apikey"]).pipe(function(a) {
                if (a !== false) {
                    self.api_key = a;
                    return true;
                } else {
                    return $.Deferred().reject();
                }
            });
        },
    });
    
                /*return new instance.web.Model("ir.config_parameter").call("set_param", ["web.linkedin.apikey", "cxnr0l53n73x"]).pipe(function() {
                    return self.test_linkedin();
                });*/
    
    instance.web_linkedin.tester = new instance.web_linkedin.LinkedinTester();
    
    instance.web_linkedin.Linkedin = instance.web.form.FieldChar.extend({
        init: function() {
            this._super.apply(this, arguments);
            var self = this;
            this.display_dm = new instance.web.DropMisordered(true);
        },
        initialize_content: function() {
            this._super();
            var $ht = $(QWeb.render("FieldChar.linkedin"));
            var $in = this.$("input");
            $in.replaceWith($ht);
            this.$(".oe_linkedin_input").append($in);
            this.$(".oe_linkedin_img").click(_.bind(this.search_linkedin, this));

        },
        search_linkedin: function() {
            var self = this;
            this.display_dm.add(instance.web_linkedin.tester.test_linkedin()).then(function() {
                debugger;
            });
        },
    });
    instance.web.form.widgets.add('linkedin', 'instance.web_linkedin.Linkedin');
};
// vim:et fdc=0 fdl=0:
