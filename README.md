# Attack-navigator

The Attack Navigator is designed to provide basic navigation and annotation of [Attack](https://attack.mitre.org) matrices, something that people are already doing today in tools like Excel.  We've designed it to be simple and generic - you can use the Navigator to visualize your defensive coverage, your red/blue team planning, the frequency of detected techniques or anything else you want to do.  The Navigator doesn't care - it just allows you to manipulate the cells in the matrix (color coding, adding a comment, assigning a numerical value, etc.).  We thought having a simple tool that everyone could use to visualize the matrix would help make it easy to use ATT&CK.

The principal feature of the Navigator is the ability for users to define layers - custom views of the ATT&CK knowledge base - e.g. showing just those techniques for a particular platform or highlighting techniques a specific adversary has been known to use. Layers can be created interactively within the Navigator or generated programmatically and then visualized via the Navigator.

## Requirements

* [Node.js](https://nodejs.org) version 8 or greater
* [AngularCLI](https://cli.angular.io)

## Install and Run

### First time

1. Navigate to the **nav-app** directory
2. Run `npm install`

### Serve application on local machine

1. Run `ng serve` within the **nav-app** directory
2. Navigate to `localhost:4200` in browser

### Compile for use elsewhere

1. Run `ng build` within the **nav-app** directory
2. Copy files from `nav-app/dist/` directory

## Adding Custom Context Menu Options

To create custom options to the **Attack Navigator** context menu using data in the Navigator, objects must be added to the array labeled `custom_context_menu_options` in `nav-app/src/assets/config.json`. Each object must have a property **label**, which is the text displayed in the context menu, and a property **url**, which is where the user is navigated.

To utilize data on right-clicked technique in the url, parameters surrounded by double curly brackets can be added to the string. For example: using `http://www.someurl.com/{{technique_attackID}}}` as the url in the custom option would lead to `http://www.someurl.com/T1098`, if the right-clicked technique's attackID was T1098.

The following data substitutions will be parsed:

* `{{technique_attackID}}` will be substituted with the Attack ID of the technique, e.g `T1234`
* `{{technique_stixID}}` will be substituted with the STIX ID of the technique, e.g `attack-pattern--12345678-1234-1234-1234-123456789123`
* `{{technique_name}}` will be substituted with the technique name in lower case and with spaces replaced with hyphens, e.g `example-technique-name`
* `{{tactic_attackID}}` will be substituted with the Attack ID of the tactic, e.g `TA1234`
* `{{tactic_stixID}}` will be substituted with the STIX ID of the tactic, e.g `x-mitre-tactic--12345678-1234-1234-1234-123456789123`
* `{{tactic_name}}` will be substituted with the tactic name in lower case and with spaces replaced with hyphens, e.g `example-tactic`. This is also equivalent to the x_mitre_shortname property of the tactic.

Optionally, a `subtechnique_url` field may be added to a custom option. This field will be parsed when the option is used on a sub-technique instead of the normal URL, which will be used for techniques. If `subtechnique_url` is not used, the `technique_` substitutions defined above will refer to the sub-technique object itself.

The following substitutions will be parsed for sub-techniques:

* `{{parent_technique_attackID}}` will be substituted with the Attack ID of the sub-technique's parent, e.g `T1234`
* `{{parent_technique_stixID}}` will be substituted with the STIX ID of the sub-technique's parent, e.g `attack-pattern--12345678-1234-1234-1234-123456789123`
* `{{parent_technique_name}}` will be substituted with the name of the sub-technique's parent in lower case and with spaces replaced with hyphens, e.g `example-technique-name`
* `{{subtechnique_attackID}}` will be substituted with the Attack ID of the sub-technique, e.g `T1234.001`
* `{{subtechnique_attackID_suffix}}` will be substituted with the portion of the ATT&CK ID of the sub-technique after the delimiting period, e.g `001`
* `{{subtechnique_stixID}}` will be substituted with the STIX ID of the sub-technique, e.g `attack-pattern--98765432-9876-9876-9876-987654321987`
* `{{subtechnique_name}}` will be substituted with the sub-technique name in lower case and with spaces replaced with hyphens, e.g `example-subtechnique-name`
* `{{tactic_attackID}}` will be substituted with the Attack ID of the tactic, e.g `TA1234`
* `{{tactic_stixID}}` will be substituted with the STIX ID of the tactic, e.g `x-mitre-tactic--12345678-1234-1234-1234-123456789123`
* `{{tactic_name}}` will be substituted with the tactic name in lower case and with spaces replaced with hyphens, e.g `example-tactic`. This is also equivalent to the x_mitre_shortname property of the tactic.

Example custom context menu objects:

```json
{
    "label": "view technique on Attack website",
    "url": "https://attack.mitre.org/techniques/{{technique_attackID}}",
    "subtechnique_url": "https://attack.mitre.org/techniques/{{parent_technique_attackID}}/{{subtechnique_attackID_suffix}}"
}
```

```json
{
    "label": "view tactic on Attack website",
    "url": "https://attack.mitre.org/tactics/{{tactic_attackID}}"
}
```
## Running the Docker File

1. Navigate to the directory where you checked out the git repository
2. Run `docker build -t yourcustomname .`
3. Run `docker run -p 4200:4200 yourcustomname`
4. Navigate to `localhost:4200` in browser
