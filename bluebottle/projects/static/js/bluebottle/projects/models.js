/* Embedded properties */

App.Adapter.map('App.Project', {
    owner: {embedded: 'load'},
    country: {embedded: 'load'},
    meta: {embedded: 'load'}
});

App.Adapter.map('App.ProjectPreview', {
    campaign: {embedded: 'load'},
    country: {embedded: 'load'}
});

App.Adapter.map('App.MyProject', {
    budgetLines: {embedded: 'load'},
    tags: {embedded: 'always'}
});

App.Adapter.map('App.PartnerOrganization', {
    projects: {embedded: 'load'}
});

App.Adapter.map('App.ProjectDonation', {
    member: {embedded: 'both'}
});

App.ProjectCountry = DS.Model.extend({
    name: DS.attr('string'),
    subregion: DS.attr('string')
});

/* Models */

App.Project = DS.Model.extend({
    url: 'projects/projects',

    // Model fields
    slug: DS.attr('string'),
    phase: DS.attr('string'),
    created: DS.attr('date'),

    owner: DS.belongsTo('App.UserPreview'),

    // Basics
    title: DS.attr('string'),
    pitch: DS.attr('string'),
    theme: DS.belongsTo('App.Theme'),
    need: DS.attr('string'),
    tags: DS.hasMany('App.Tag'),

    // Description
    description: DS.attr('string'),
    effects: DS.attr('string'),
    future: DS.attr('string'),
    for_who: DS.attr('string'),
    reach: DS.attr('number'),

    // Location
    country: DS.belongsTo('App.ProjectCountry'),
    latitude: DS.attr('string'),
    longitude: DS.attr('string'),

    // Media
    image: DS.attr('image'),

    // Budget
    budgetLines: DS.hasMany('App.BudgetLine'),

    isPhasePlan: Em.computed.equal('phase', 'plan'),
    isPhaseCampaign: Em.computed.equal('phase', 'campaign'),
    isPhaseDone: Em.computed.equal('phase', 'failed'),

    getProject: function(){
        return App.Project.find(this.get('id'));
    }.property('id'),

    daysToGo: function(){
        if (!this.get('time')) {
            return null;
        }
        var now = new Date();
        var microseconds = this.get('deadline').getTime() - now.getTime();
        return Math.ceil(microseconds / (1000 * 60 * 60 * 24));
    }.property('deadline')

});


App.ProjectPreview = App.Project.extend({
    url: 'projects/previews',
    image: DS.attr('string'),
    country: DS.belongsTo('App.ProjectCountry'),
    pitch: DS.attr('string')
});


App.ProjectSearch = DS.Model.extend({

    text: DS.attr('string'),
    country: DS.attr('number'),
    theme:  DS.attr('number'),
    ordering: DS.attr('string', {defaultValue: 'popularity'}),
    phase: DS.attr('string', {defaultValue: 'campaign'}),
    page: DS.attr('number', {defaultValue: 1})

});

// TODO: Refactor App.DonationPreview to ProjectSupporter
App.DonationPreview = DS.Model.extend({
    url: 'projects/supporters',

    project: DS.belongsTo('App.ProjectPreview'),
    member: DS.belongsTo('App.UserPreview'),
    date_donated: DS.attr('date'),

    time_since: function(){
        return Globalize.format(this.get('date_donated'), 'X');
    }.property('date_donated')
});


App.ProjectDonation = DS.Model.extend({
    url: 'projects/donations',

    member: DS.belongsTo('App.UserPreview'),
    amount: DS.attr('number'),
    date_donated: DS.attr('date'),

    time_since: function(){
        return Globalize.format(this.get('date_donated'), 'X');
    }.property('date_donated')
});



App.Theme = DS.Model.extend({
    url:'projects/themes',
    title: DS.attr('string')
});

App.ThemeList = [
    {id: "0", title: gettext("--loading--")}
];


/* Project Manage Models */

App.MyProjectBudgetLine = DS.Model.extend({
    url: 'projects/budgetlines/manage',

    project: DS.belongsTo('App.MyProject'),
    description: DS.attr('string'),
    amount: DS.attr('number')
});


App.BudgetLine = DS.Model.extend({
    project: DS.belongsTo('App.Project'),
    description: DS.attr('string'),
    amount: DS.attr('number')
});


App.MyProject = App.Project.extend({
    url: 'projects/manage',

    // Basics
    title: DS.attr('string'),
    pitch: DS.attr('string'),
    theme: DS.attr('string'),
    need: DS.attr('string'),
    tags: DS.hasMany('App.Tag'),

    editable: DS.attr('boolean'),

    validBasics: function(){
        if (this.get('title') &&  this.get('pitch') && this.get('theme') && this.get('tags.length')){
            return true;
        }
        return false;
    }.property('title', 'pitch', 'theme', 'tags'),

    // Description
    description: DS.attr('string'),
    reach: DS.attr('number'),

    validDescription: function(){
        if (this.get('description') && this.get('reach')){
            return true;
        }
        return false;
    }.property('description', 'reach'),

    // Media
    image: DS.attr('image'),
    video_url: DS.attr('string'),
    video_html: DS.attr('string'),


    // Location
    country: DS.attr('string'),
    latitude: DS.attr('string'),
    longitude: DS.attr('string'),

    validLocation: function(){
        if (this.get('country') &&  this.get('latitude') && this.get('longitude')){
            return true;
        }
        return false;
    }.property('country', 'latitude', 'longitude'),


    validMedia: function(){
        if (this.get('image')){
            return true;
        }
        return false;
    }.property('image'),

    // Crowd funding
    moneyNeeded: DS.attr('string'),
    budgetLines: DS.hasMany('App.MyProjectBudgetLine'),

    totalBudget: function(){
        var lines = this.get('budgetLines');
        return lines.reduce(function(prev, line){
            return (prev || 0) + (line.get('amount')/1 || 0);
        });
    }.property('budgetLines.@each.amount'),

    validBudget: function(){
        if (this.get('totalBudget') > 0 &&  this.get('totalBudget') <= 5000 ){
            return true;
        }
        return false;
    }.property('totalBudget'),

    created: DS.attr('date'),

    organization: DS.belongsTo('App.MyOrganization')

});