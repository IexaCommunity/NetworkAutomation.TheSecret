# NetworkAutomation.TheSecret
A collection of scripts used in the document "Network Automation. The Secret", developed by IeXa Academy

The main goal of the document is to analyze a rundown of network automation tools, in order to define the core functionalities you need to consider when you have to project a network automation solution on your own.

The lab environment we used includes:
<ul>
  <li>A control machine, through an Ubuntu 20.04 LTS virtual machine in VMware Workstation 15;</li>
  <li>A Cisco IOS XE router, virtualized in VMware Worstation 15.</li>
</ul>

The networking setup relies on the usage of the NAT mode, through the default VMnet8.

The document contains many examples, since it shows the evolution of scripting to automate network activities, from screen scraping tools till the more recent Model-Driven protocols and applications.
In particular, in the first release we used:
<ol>
  <li>A bash script</li>
  <li>An expect script</li>
  <li>A VBScript with SecureCRT script</li>
  <li>A Python script with Paramiko</li>
  <li>A Python script with Netmiko</li>
  <li>A Python script with Napalm</li>
  <li>A Python script with Ncclient</li>
  <li>A Python script with Requests</li>
</ol>
