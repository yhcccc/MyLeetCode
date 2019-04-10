```py
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        loc_list = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            valid = local_name.split('+')[0]
            valid = valid.split('.')
            loc_f = ''.join(valid)
            loc_list.add(loc_f+domain_name)
        return len(loc_list)
```
