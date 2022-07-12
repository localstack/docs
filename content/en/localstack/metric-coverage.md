---
title: "LocalStack Coverage"
linkTitle: "LocalStack Coverage"
weight: 100
description: >
  Overview of the implemented AWS APIs in LocalStack
---



<div class="coverage-report">


## ec2 ##

<table>
  <thead>
    <tr>
      <th>Operation</th>
      <th style="text-align:right">Implemented</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>AcceptTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AcceptVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AllocateAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssignIpv6Addresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssignPrivateIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateIamInstanceProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateSubnetCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AssociateVpcCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachInternetGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AttachVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeSecurityGroupEgress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>AuthorizeSecurityGroupIngress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelSpotFleetRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CancelSpotInstanceRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopyImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CopySnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCarrierGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateCustomerGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateEgressOnlyInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateImage <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateInternetGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateKeyPair <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateLaunchTemplateVersion</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNatGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkAcl</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreatePlacementGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSpotDatafeedSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateSubnet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTags <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpc <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcEndpoint <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcEndpointServiceConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpnConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>CreateVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCarrierGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteCustomerGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteEgressOnlyInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteKeyPair</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteLaunchTemplate</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNatGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkAcl</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeletePlacementGroup</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRoute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSecurityGroup <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSnapshot</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSpotDatafeedSubscription</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteSubnet <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpc <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpointServiceConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpcPeeringConnection <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpnConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeleteVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DeregisterImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAccountAttributes <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeAvailabilityZones</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCarrierGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeCustomerGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeDhcpOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeEgressOnlyInternetGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeFlowLogs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeIamInstanceProfileAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeImages <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceCreditSpecifications</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceStatus</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceTypeOfferings</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstanceTypes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeInternetGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeKeyPairs</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchTemplateVersions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeLaunchTemplates</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeManagedPrefixLists</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNatGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkAcls <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfaces <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribePrefixLists</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRegions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReservedInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesOfferings <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeRouteTables <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroups <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSnapshots</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotInstanceRequests</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSpotPriceHistory</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeSubnets <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTags</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayPeeringAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayRouteTables</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayVpcAttachments</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeTransitGateways</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVolumes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcAttribute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcClassicLink <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcClassicLinkDnsSupport <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServiceConfigurations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServicePermissions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointServices <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpoints <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcPeeringConnections <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpcs <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpnConnections</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DescribeVpnGateways <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachInternetGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachNetworkInterface</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DetachVpnGateway <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableTransitGatewayRouteTablePropagation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableVpcClassicLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisableVpcClassicLinkDnsSupport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateAddress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateIamInstanceProfile</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateRouteTable <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateSubnetCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateTransitGatewayRouteTable</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>DisassociateVpcCidrBlock</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableTransitGatewayRouteTablePropagation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVolumeIO</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVpcClassicLink</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>EnableVpcClassicLinkDnsSupport</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetConsoleOutput</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetEbsEncryptionByDefault</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetManagedPrefixListEntries</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTransitGatewayRouteTableAssociations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>GetTransitGatewayRouteTablePropagations</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportKeyPair <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ImportVolume</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyInstanceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyManagedPrefixList</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySpotFleetRequest</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifySubnetAttribute <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTransitGateway</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyTransitGatewayVpcAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVolumeAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpoint</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServiceConfiguration</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServicePermissions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcPeeringConnectionOptions</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ModifyVpcTenancy</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>MonitorInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>PurchaseReservedInstancesOffering <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RebootInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RegisterImage</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayPeeringAttachment</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RejectVpcPeeringConnection</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReleaseAddress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceIamInstanceProfileAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceNetworkAclAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceNetworkAclEntry</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceRoute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ReplaceRouteTableAssociation</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RequestSpotFleet</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RequestSpotInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetImageAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetNetworkInterfaceAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>ResetSnapshotAttribute</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokeSecurityGroupEgress <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RevokeSecurityGroupIngress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>RunInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>SearchTransitGatewayRoutes</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StartInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>StopInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>TerminateInstances <a href="#misc" title="covered by our integration test suite">✨</a></td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnassignIpv6Addresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnassignPrivateIpAddresses</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UnmonitorInstances</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecurityGroupRuleDescriptionsEgress</td>
       <td style="text-align:right">✅</td>
    </tr>
    <tr>
      <td>UpdateSecurityGroupRuleDescriptionsIngress</td>
       <td style="text-align:right">✅</td>
    </tr>
    </tbody>
    <tobdy>
    <tr>
      <td><a data-toggle="collapse" href=".ec2-notimplemented">Show more</a></td>
      <td style="text-align:right"></td>
    </tr>
    </tbody>
    <tbody class="collapse ec2-notimplemented">
    <tr>
      <td>AcceptReservedInstancesExchangeQuote</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AcceptTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AcceptTransitGatewayVpcAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AcceptVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AdvertiseByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AllocateHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AllocateIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ApplySecurityGroupsToClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AssociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AttachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>AuthorizeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>BundleInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelBundleTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelConversionTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelImportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CancelReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ConfirmProductInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CopyFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDefaultSubnet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateDefaultVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateInstanceExportTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreatePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReplaceRootVolumeTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateReservedInstancesListing</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateRestoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateStoreImageTask</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>CreateVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteClientVpnRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteFpgaImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLaunchTemplateVersions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteLocalGatewayRouteTableVpcAssociation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAccessScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInsightsPath</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteNetworkInterfacePermission</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeletePublicIpv4Pool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteQueuedReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteSubnetCidrReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorFilter</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTrafficMirrorTarget</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayConnect</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayConnectPeer</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeleteVpnConnectionRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeprovisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DeregisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAddressesAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeAggregateIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeBundleTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeByoipCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCapacityReservationFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCapacityReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClassicLinkInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnAuthorizationRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnEndpoints</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeClientVpnTargetNetworks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeCoipPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeConversionTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeElasticGpus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeExportTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFastLaunchImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFleetHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFleetInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFleets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeFpgaImages</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHostReservationOfferings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHostReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImportImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeImportSnapshotTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeInstanceEventWindows</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpamPools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpamScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpams</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeIpv6Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTableVpcAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayRouteTables</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayVirtualInterfaceGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGatewayVirtualInterfaces</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeLocalGateways</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeMovingAddresses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAccessScopeAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAccessScopes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsAnalyses</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInsightsPaths</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeNetworkInterfacePermissions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePlacementGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePrincipalIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribePublicIpv4Pools</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReplaceRootVolumeTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesListings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeReservedInstancesModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledInstanceAvailability</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroupReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSnapshotTierStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSpotDatafeedSubscription</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeSpotFleetRequestHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStaleSecurityGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeStoreImageTasks</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorFilters</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorSessions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrafficMirrorTargets</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayConnectPeers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayConnects</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTransitGatewayMulticastDomains</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeTrunkInterfaceAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVolumeAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVolumeStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVolumesModifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointConnectionNotifications</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DescribeVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DetachClassicLinkVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateClientVpnTargetNetwork</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateEnclaveCertificateIamRole</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateTransitGatewayMulticastDomain</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>DisassociateTrunkInterface</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableFastLaunch</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableFastSnapshotRestores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableImageDeprecation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableIpamOrganizationAdminAccount</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableSerialConsoleAccess</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>EnableVgwRoutePropagation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportClientVpnClientConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ExportTransitGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAssociatedEnclaveCertificateIamRoles</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetAssociatedIpv6PoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCapacityReservationUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetCoipPoolUsage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetConsoleScreenshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetFlowLogsIntegrationTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetGroupsForCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetHostReservationPurchasePreview</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInstanceTypesFromInstanceRequirements</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetInstanceUefiData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamAddressHistory</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamPoolAllocations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamPoolCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetIpamResourceCidrs</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetLaunchTemplateData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetManagedPrefixListAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetNetworkInsightsAccessScopeAnalysisFindings</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetNetworkInsightsAccessScopeContent</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetPasswordData</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetReservedInstancesExchangeQuote</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSerialConsoleAccessStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSpotPlacementScores</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetSubnetCidrReservations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayAttachmentPropagations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetTransitGatewayPrefixListReferences</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVpnConnectionDeviceSampleConfiguration</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>GetVpnConnectionDeviceTypes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportClientVpnClientCertificateRevocationList</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportImage</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportInstance</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ImportSnapshot</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListImagesInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ListSnapshotsInRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyAvailabilityZoneGroup</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyCapacityReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyCapacityReservationFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyClientVpnEndpoint</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyDefaultCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyFleet</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIdentityIdFormat</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceCapacityReservationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceCreditSpecification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceEventStartTime</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceEventWindow</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceMaintenanceOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstanceMetadataOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyInstancePlacement</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamPool</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamResourceCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyIpamScope</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyLaunchTemplate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyPrivateDnsNameOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyReservedInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifySecurityGroupRules</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifySnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorFilterNetworkServices</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorFilterRule</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTrafficMirrorSession</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyTransitGatewayPrefixListReference</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVolume</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointConnectionNotification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpcEndpointServicePayerResponsibility</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnConnection</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnConnectionOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnTunnelCertificate</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ModifyVpnTunnelOptions</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MoveAddressToVpc</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>MoveByoipCidrToIpam</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionIpamPoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ProvisionPublicIpv4PoolCidr</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseHostReservation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>PurchaseScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterInstanceEventNotificationAttributes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTransitGatewayMulticastGroupMembers</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RegisterTransitGatewayMulticastGroupSources</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayMulticastDomainAssociations</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectTransitGatewayVpcAttachment</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RejectVpcEndpointConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReleaseHosts</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReleaseIpamPoolAllocation</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReplaceTransitGatewayRoute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ReportInstanceStatus</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetAddressAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetEbsDefaultKmsKeyId</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetFpgaImageAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>ResetInstanceAttribute</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreAddressToClassic</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreImageFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreManagedPrefixListVersion</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreSnapshotFromRecycleBin</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RestoreSnapshotTier</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RevokeClientVpnIngress</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>RunScheduledInstances</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchLocalGatewayRoutes</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SearchTransitGatewayMulticastGroups</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>SendDiagnosticInterrupt</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartNetworkInsightsAccessScopeAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartNetworkInsightsAnalysis</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>StartVpcEndpointServicePrivateDnsVerification</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>TerminateClientVpnConnections</td>
       <td style="text-align:right">-</td>
    </tr>
    <tr>
      <td>WithdrawByoipCidr</td>
       <td style="text-align:right">-</td>
    </tr>
 </tbody>
</table>
