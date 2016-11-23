/*
+--------------------------------------------------------------------------
|   [HSC] Topic Templates 2.0
|   =============================================
|   by Esther Eisner
|   Copyright 2010 HeadStand Consulting
|   esther@headstandconsulting.com
+--------------------------------------------------------------------------
*/

var _topicTemplate = window.IPBoard;

_topicTemplate.prototype.topicTemplate = {
    
    init: function()
    {
        document.observe("dom:loaded", function()
        {
            ipb.topicTemplate.initEvents();
        });
    },
    
    initEvents: function()
    {
        if($('set_id'))
        {
            if($F('set_id') > 0)
                ipb.topicTemplate.getTemplate();
            
            $('set_id').observe('change', ipb.topicTemplate.getTemplate);
        }            
    },
    
    getTemplate: function(e)
    {
        var setId = $('set_id').value;
        
        if(setId==0)
        {
            $('set_description').update('');
            $('set_description').removeClassName('message');
            $('set_fields').update('');
            return;
        }
        
        var url = ipb.vars['base_url'] + 'app=topictemplate&module=ajax&section=sets&do=get&md5check=' + ipb.vars['secure_hash'];
        
        new Ajax.Request(url,
                        {
                            method: 'post',
                            parameters: {
                                set_id: setId,
                                forum_id: ipb.topicTemplate.forumId,
                                topic_id: ipb.topicTemplate.topicId
                            },
                            onSuccess: function(t)
                            {
                                if(t.responseJSON['description'])
                                {
                                    $('set_description').addClassName('message');
                                    $('set_description').update(t.responseJSON['description']);
                                }
                                else
                                {
                                    $('set_description').removeClassName('message');
                                    $('set_description').update('');
                                }
                                
                                if(t.responseJSON['template'])
                                {
                                    $('set_fields').update(t.responseJSON['template']);
                                    $$("[data-tooltip]").invoke('tooltip');
                                }
                                else
                                {
                                    $('set_fields').update('');
                                }
                            }
                        });        
    },
}

ipb.topicTemplate.init();