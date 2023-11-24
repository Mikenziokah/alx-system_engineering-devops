#  Puppet, create a manifest that kills a process named killmenow
exec {'killmenow':
  command  => 'killmenow',
  provider => 'shell'
  returns  => [0, 1],
}
