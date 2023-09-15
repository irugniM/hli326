{"payload":{"allShortcutsEnabled":false,"fileTree":{"":{"items":[{"name":"README.md","path":"README.md","contentType":"file"},{"name":"sample.py","path":"sample.py","contentType":"file"}],"totalCount":2}},"fileTreeProcessingTime":2.77622,"foldersToFetch":[],"reducedMotionEnabled":null,"repo":{"id":447074693,"defaultBranch":"main","name":"ops445-lab1","ownerLogin":"ahadalioglu","currentUserCanPush":false,"isFork":false,"isEmpty":false,"createdAt":"2022-01-12T04:22:32.000Z","ownerAvatar":"https://avatars.githubusercontent.com/u/65471600?v=4","public":true,"private":false,"isOrgOwned":false},"symbolsExpanded":false,"treeExpanded":true,"refInfo":{"name":"main","listCacheKey":"v0:1641961402.757913","canEdit":false,"refType":"branch","currentOid":"6f79933000469fedbab0db14ed361558fa52bdc2"},"path":"sample.py","currentUser":null,"blob":{"rawLines":["#!/usr/bin/env python3\r","'''Sample Python script for OPS445 Lab 1.\r","   Author: Raymond Chan\r","   Program name: sample.py\r","   Date Created: May 2020\r","\r","   Usage: sample.py [base_name]\r","\r","   A list of subdictories will be created under $HOME/[base_name]/dir_list\r","   '''\r","\r","import sys\r","import os\r","\r","def summary(s,k,e):\r","    '''Format and return summary information\r","       function parameters:\r","       s - success\r","       k - skipped\r","       e - error \r","       function return a formatted string '''\r","    hc = '|'\r","    vc = '|'\r","    headers = {'Success':str(s),'Skipped':str(k),'Error':str(e)}\r","    for header in headers.keys():\r","        hc = hc + header.center(len(header)+4,'-') + '|'\r","        vc = vc + headers[header].center(len(header)+4,' ') + '|'\r","    return hc + '\\n' + vc\r","\r","if __name__ == '__main__':\r","    # check command line arguments\r","    if len(sys.argv) == 1:\r","        base_dir = os.getenv('HOME')\r","    else:\r","        base_dir = os.getenv('HOME')+'/'+sys.argv[1]\r","\r","    print('Base Directory:',base_dir)\r","\r","    dir_list = [ 'lab1',\r","                 'lab2',\r","                 'lab3',\r","                 'lab4',\r","                 'lab5',\r","                 'lab6',\r","                 'lab7',\r","                 'lab8',\r","                 'a1',\r","                 'a2' ]\r","\r","    success_count = 0\r","    fail_count = 0\r","    error_count = 0\r","\r","    for sub_dir in dir_list:\r","        sub_dir_path = base_dir + '/ops445/' + sub_dir\r","        if os.path.isdir(sub_dir_path) == True:\r","            print('Subdirectory',sub_dir_path,'already exist, skipped.',file=sys.stderr)\r","            fail_count += 1\r","        else:\r","            try:\r","                os.mkdir(sub_dir_path,mode=0o755)\r","                print('Subdirectory',sub_dir_path,'created.')\r","                success_count += 1\r","            except:\r","                print('Trouble creating',sub_dir_path,'- directory not created.',file=sys.stderr)\r","                error_count += 1\r","    \r","    print('Script execution summary:')\r","    print(summary(success_count,fail_count,error_count))\r"],"stylingDirectives":[[{"start":0,"end":23,"cssClass":"pl-c"}],[{"start":0,"end":42,"cssClass":"pl-s"}],[{"start":0,"end":24,"cssClass":"pl-s"}],[{"start":0,"end":27,"cssClass":"pl-s"}],[{"start":0,"end":26,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s"}],[{"start":0,"end":32,"cssClass":"pl-s"}],[{"start":0,"end":1,"cssClass":"pl-s"}],[{"start":0,"end":75,"cssClass":"pl-s"}],[{"start":0,"end":6,"cssClass":"pl-s"}],[],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-s1"}],[{"start":0,"end":6,"cssClass":"pl-k"},{"start":7,"end":9,"cssClass":"pl-s1"}],[],[{"start":0,"end":3,"cssClass":"pl-k"},{"start":4,"end":11,"cssClass":"pl-en"},{"start":12,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-s1"}],[{"start":4,"end":45,"cssClass":"pl-s"}],[{"start":0,"end":28,"cssClass":"pl-s"}],[{"start":0,"end":19,"cssClass":"pl-s"}],[{"start":0,"end":19,"cssClass":"pl-s"}],[{"start":0,"end":18,"cssClass":"pl-s"}],[{"start":0,"end":45,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-s"}],[{"start":4,"end":6,"cssClass":"pl-s1"},{"start":7,"end":8,"cssClass":"pl-c1"},{"start":9,"end":12,"cssClass":"pl-s"}],[{"start":4,"end":11,"cssClass":"pl-s1"},{"start":12,"end":13,"cssClass":"pl-c1"},{"start":15,"end":24,"cssClass":"pl-s"},{"start":25,"end":28,"cssClass":"pl-en"},{"start":29,"end":30,"cssClass":"pl-s1"},{"start":32,"end":41,"cssClass":"pl-s"},{"start":42,"end":45,"cssClass":"pl-en"},{"start":46,"end":47,"cssClass":"pl-s1"},{"start":49,"end":56,"cssClass":"pl-s"},{"start":57,"end":60,"cssClass":"pl-en"},{"start":61,"end":62,"cssClass":"pl-s1"}],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":14,"cssClass":"pl-s1"},{"start":15,"end":17,"cssClass":"pl-c1"},{"start":18,"end":25,"cssClass":"pl-s1"},{"start":26,"end":30,"cssClass":"pl-en"}],[{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":24,"cssClass":"pl-s1"},{"start":25,"end":31,"cssClass":"pl-en"},{"start":32,"end":35,"cssClass":"pl-en"},{"start":36,"end":42,"cssClass":"pl-s1"},{"start":43,"end":44,"cssClass":"pl-c1"},{"start":44,"end":45,"cssClass":"pl-c1"},{"start":46,"end":49,"cssClass":"pl-s"},{"start":51,"end":52,"cssClass":"pl-c1"},{"start":53,"end":56,"cssClass":"pl-s"}],[{"start":8,"end":10,"cssClass":"pl-s1"},{"start":11,"end":12,"cssClass":"pl-c1"},{"start":13,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":25,"cssClass":"pl-s1"},{"start":26,"end":32,"cssClass":"pl-s1"},{"start":34,"end":40,"cssClass":"pl-en"},{"start":41,"end":44,"cssClass":"pl-en"},{"start":45,"end":51,"cssClass":"pl-s1"},{"start":52,"end":53,"cssClass":"pl-c1"},{"start":53,"end":54,"cssClass":"pl-c1"},{"start":55,"end":58,"cssClass":"pl-s"},{"start":60,"end":61,"cssClass":"pl-c1"},{"start":62,"end":65,"cssClass":"pl-s"}],[{"start":4,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":15,"cssClass":"pl-c1"},{"start":16,"end":20,"cssClass":"pl-s"},{"start":17,"end":19,"cssClass":"pl-cce"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":25,"cssClass":"pl-s1"}],[],[{"start":0,"end":2,"cssClass":"pl-k"},{"start":3,"end":11,"cssClass":"pl-s1"},{"start":12,"end":14,"cssClass":"pl-c1"},{"start":15,"end":25,"cssClass":"pl-s"}],[{"start":4,"end":35,"cssClass":"pl-c"}],[{"start":4,"end":6,"cssClass":"pl-k"},{"start":7,"end":10,"cssClass":"pl-en"},{"start":11,"end":14,"cssClass":"pl-s1"},{"start":15,"end":19,"cssClass":"pl-s1"},{"start":21,"end":23,"cssClass":"pl-c1"},{"start":24,"end":25,"cssClass":"pl-c1"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":21,"cssClass":"pl-s1"},{"start":22,"end":28,"cssClass":"pl-en"},{"start":29,"end":35,"cssClass":"pl-s"}],[{"start":4,"end":8,"cssClass":"pl-k"}],[{"start":8,"end":16,"cssClass":"pl-s1"},{"start":17,"end":18,"cssClass":"pl-c1"},{"start":19,"end":21,"cssClass":"pl-s1"},{"start":22,"end":28,"cssClass":"pl-en"},{"start":29,"end":35,"cssClass":"pl-s"},{"start":36,"end":37,"cssClass":"pl-c1"},{"start":37,"end":40,"cssClass":"pl-s"},{"start":40,"end":41,"cssClass":"pl-c1"},{"start":41,"end":44,"cssClass":"pl-s1"},{"start":45,"end":49,"cssClass":"pl-s1"},{"start":50,"end":51,"cssClass":"pl-c1"}],[],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":27,"cssClass":"pl-s"},{"start":28,"end":36,"cssClass":"pl-s1"}],[],[{"start":4,"end":12,"cssClass":"pl-s1"},{"start":13,"end":14,"cssClass":"pl-c1"},{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":23,"cssClass":"pl-s"}],[{"start":17,"end":21,"cssClass":"pl-s"}],[{"start":17,"end":21,"cssClass":"pl-s"}],[],[{"start":4,"end":17,"cssClass":"pl-s1"},{"start":18,"end":19,"cssClass":"pl-c1"},{"start":20,"end":21,"cssClass":"pl-c1"}],[{"start":4,"end":14,"cssClass":"pl-s1"},{"start":15,"end":16,"cssClass":"pl-c1"},{"start":17,"end":18,"cssClass":"pl-c1"}],[{"start":4,"end":15,"cssClass":"pl-s1"},{"start":16,"end":17,"cssClass":"pl-c1"},{"start":18,"end":19,"cssClass":"pl-c1"}],[],[{"start":4,"end":7,"cssClass":"pl-k"},{"start":8,"end":15,"cssClass":"pl-s1"},{"start":16,"end":18,"cssClass":"pl-c1"},{"start":19,"end":27,"cssClass":"pl-s1"}],[{"start":8,"end":20,"cssClass":"pl-s1"},{"start":21,"end":22,"cssClass":"pl-c1"},{"start":23,"end":31,"cssClass":"pl-s1"},{"start":32,"end":33,"cssClass":"pl-c1"},{"start":34,"end":44,"cssClass":"pl-s"},{"start":45,"end":46,"cssClass":"pl-c1"},{"start":47,"end":54,"cssClass":"pl-s1"}],[{"start":8,"end":10,"cssClass":"pl-k"},{"start":11,"end":13,"cssClass":"pl-s1"},{"start":14,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":25,"end":37,"cssClass":"pl-s1"},{"start":39,"end":41,"cssClass":"pl-c1"},{"start":42,"end":46,"cssClass":"pl-c1"}],[{"start":12,"end":17,"cssClass":"pl-en"},{"start":18,"end":32,"cssClass":"pl-s"},{"start":33,"end":45,"cssClass":"pl-s1"},{"start":46,"end":71,"cssClass":"pl-s"},{"start":72,"end":76,"cssClass":"pl-s1"},{"start":76,"end":77,"cssClass":"pl-c1"},{"start":77,"end":80,"cssClass":"pl-s1"},{"start":81,"end":87,"cssClass":"pl-s1"}],[{"start":12,"end":22,"cssClass":"pl-s1"},{"start":23,"end":25,"cssClass":"pl-c1"},{"start":26,"end":27,"cssClass":"pl-c1"}],[{"start":8,"end":12,"cssClass":"pl-k"}],[{"start":12,"end":15,"cssClass":"pl-k"}],[{"start":16,"end":18,"cssClass":"pl-s1"},{"start":19,"end":24,"cssClass":"pl-en"},{"start":25,"end":37,"cssClass":"pl-s1"},{"start":38,"end":42,"cssClass":"pl-s1"},{"start":42,"end":43,"cssClass":"pl-c1"},{"start":43,"end":48,"cssClass":"pl-c1"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":36,"cssClass":"pl-s"},{"start":37,"end":49,"cssClass":"pl-s1"},{"start":50,"end":60,"cssClass":"pl-s"}],[{"start":16,"end":29,"cssClass":"pl-s1"},{"start":30,"end":32,"cssClass":"pl-c1"},{"start":33,"end":34,"cssClass":"pl-c1"}],[{"start":12,"end":18,"cssClass":"pl-k"}],[{"start":16,"end":21,"cssClass":"pl-en"},{"start":22,"end":40,"cssClass":"pl-s"},{"start":41,"end":53,"cssClass":"pl-s1"},{"start":54,"end":80,"cssClass":"pl-s"},{"start":81,"end":85,"cssClass":"pl-s1"},{"start":85,"end":86,"cssClass":"pl-c1"},{"start":86,"end":89,"cssClass":"pl-s1"},{"start":90,"end":96,"cssClass":"pl-s1"}],[{"start":16,"end":27,"cssClass":"pl-s1"},{"start":28,"end":30,"cssClass":"pl-c1"},{"start":31,"end":32,"cssClass":"pl-c1"}],[],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":37,"cssClass":"pl-s"}],[{"start":4,"end":9,"cssClass":"pl-en"},{"start":10,"end":17,"cssClass":"pl-en"},{"start":18,"end":31,"cssClass":"pl-s1"},{"start":32,"end":42,"cssClass":"pl-s1"},{"start":43,"end":54,"cssClass":"pl-s1"}]],"csv":null,"csvError":null,"dependabotInfo":{"showConfigurationBanner":false,"configFilePath":null,"networkDependabotPath":"/ahadalioglu/ops445-lab1/network/updates","dismissConfigurationNoticePath":"/settings/dismiss-notice/dependabot_configuration_notice","configurationNoticeDismissed":null,"repoAlertsPath":"/ahadalioglu/ops445-lab1/security/dependabot","repoSecurityAndAnalysisPath":"/ahadalioglu/ops445-lab1/settings/security_analysis","repoOwnerIsOrg":false,"currentUserCanAdminRepo":false},"displayName":"sample.py","displayUrl":"https://github.com/ahadalioglu/ops445-lab1/blob/main/sample.py?raw=true","headerInfo":{"blobSize":"1.99 KB","deleteInfo":{"deleteTooltip":"You must be signed in to make or propose changes"},"editInfo":{"editTooltip":"You must be signed in to make or propose changes"},"ghDesktopPath":"https://desktop.github.com","gitLfsPath":null,"onBranch":true,"shortPath":"f4556e9","siteNavLoginPath":"/login?return_to=https%3A%2F%2Fgithub.com%2Fahadalioglu%2Fops445-lab1%2Fblob%2Fmain%2Fsample.py","isCSV":false,"isRichtext":false,"toc":null,"lineInfo":{"truncatedLoc":"69","truncatedSloc":"59"},"mode":"file"},"image":false,"isCodeownersFile":null,"isPlain":false,"isValidLegacyIssueTemplate":false,"issueTemplateHelpUrl":"https://docs.github.com/articles/about-issue-and-pull-request-templates","issueTemplate":null,"discussionTemplate":null,"language":"Python","languageID":303,"large":false,"loggedIn":false,"newDiscussionPath":"/ahadalioglu/ops445-lab1/discussions/new","newIssuePath":"/ahadalioglu/ops445-lab1/issues/new","planSupportInfo":{"repoIsFork":null,"repoOwnedByCurrentUser":null,"requestFullPath":"/ahadalioglu/ops445-lab1/blob/main/sample.py","showFreeOrgGatedFeatureMessage":null,"showPlanSupportBanner":null,"upgradeDataAttributes":null,"upgradePath":null},"publishBannersInfo":{"dismissActionNoticePath":"/settings/dismiss-notice/publish_action_from_dockerfile","dismissStackNoticePath":"/settings/dismiss-notice/publish_stack_from_file","releasePath":"/ahadalioglu/ops445-lab1/releases/new?marketplace=true","showPublishActionBanner":false,"showPublishStackBanner":false},"renderImageOrRaw":false,"richText":null,"renderedFileInfo":null,"shortPath":null,"tabSize":8,"topBannersInfo":{"overridingGlobalFundingFile":false,"globalPreferredFundingPath":null,"repoOwner":"ahadalioglu","repoName":"ops445-lab1","showInvalidCitationWarning":false,"citationHelpUrl":"https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/creating-a-repository-on-github/about-citation-files","showDependabotConfigurationBanner":false,"actionsOnboardingTip":null},"truncated":false,"viewable":true,"workflowRedirectUrl":null,"symbols":{"timedOut":false,"notAnalyzed":false,"symbols":[{"name":"summary","kind":"function","identStart":299,"identEnd":306,"extentStart":295,"extentEnd":776,"fullyQualifiedName":"summary","identUtf16":{"start":{"lineNumber":14,"utf16Col":4},"end":{"lineNumber":14,"utf16Col":11}},"extentUtf16":{"start":{"lineNumber":14,"utf16Col":0},"end":{"lineNumber":27,"utf16Col":25}}}]}},"copilotInfo":null,"csrf_tokens":{"/ahadalioglu/ops445-lab1/branches":{"post":"yKRPdovYbkrljk_aubqXRzhpd-wh7jlL1QwvuyhgTaGSwd4JvMOxGid_gYMYXvWvNi90WSf3tZ6KOSC-RCfvMw"},"/repos/preferences":{"post":"meJY_8qcgVLHYeD35xUo64wRcfn2jAxjCs7TaKoe3fIOXfix-8zEZJNTz-KNUWRm3ZvSxfjlYzQfQNFsoP_O8Q"}}},"title":"ops445-lab1/sample.py at main · ahadalioglu/ops445-lab1"}