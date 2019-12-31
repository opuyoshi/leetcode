class Solution:
    def numUniqueEmail(self, emails):
        count = 0
        dic = []
        for email in emails:
            local, domain = email.split('@')
            local = local.replace('.', '')
            if '+' in local:
                local = local[: local.find('+')]
            email = local + '@' + domain
            if email not in dic:
                dic.append(email)
                count += 1
        return count
